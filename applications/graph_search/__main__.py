from draw.button import ButtonData, PackData
from draw.tkinter_singleton import TkinterSingleton
from draw.colour import Colour

from core.dimensions import Dim2D
from core.shapes import Shape2D
from core.graph import Graph

from .utils import Status, Button, Utils, GraphData
from .path_processor import PathProcessor

def create_buttons_layer_canvas(status_dictionary):

    def create_buttons(buttons, frame):
        default_pack_data = PackData()
        for data in buttons:
            if data.pack_data is None:
                data.pack_data = default_pack_data
            TkinterSingleton.create_button_with_pack(data, frame)

    player_frame = TkinterSingleton.create_frame_with_pack(PackData(side=None))
    player_buttons = [
        ButtonData("back", Button.back, status_dictionary),
        ButtonData("next", Button.next, status_dictionary),
        ButtonData("play_forward", Button.play_forward, status_dictionary),
        ButtonData("play_backward", Button.play_backward, status_dictionary),
        ButtonData("pause", Button.pause, status_dictionary),
        ButtonData("restart", Button.restart, status_dictionary)
    ]
    create_buttons(player_buttons, player_frame)

    others_frames = TkinterSingleton.create_frame_with_pack(PackData(side=None))
    others_buttons = [
        ButtonData("reset", Button.reset, status_dictionary),
        ButtonData("options", Button.open_options, status_dictionary)
    ]
    create_buttons(others_buttons, others_frames)

def initialize_gui(graph_data: GraphData, status_dictionary):
    TkinterSingleton.create_canvas(graph_data.tile_size.vectoral_multiply(graph_data.grid_size))
    TkinterSingleton.canvas.configure(background=Colour.GREEN.value)
    TkinterSingleton.canvas.pack(fill="both", expand=True)
    create_buttons_layer_canvas(status_dictionary)
    raw_grid_data = Utils.create_rectangle_canvas(graph_data)
    TkinterSingleton.refresh()
    return raw_grid_data

def main():
    TkinterSingleton.start(title="Graph Search Program")

    # TODO: Add options data and check it
    # TODO: Set the tile size and grid size with arguments (argparse)
    tile_size = Dim2D(10, 10)
    grid_size = Dim2D(60, 60)
    status_dictionary = {
        Status.ON_PAUSE: True,
        Status.SHOULD_RESTART: False,
        Status.SHOULD_GO_BACK: False,
        Status.SHOULD_GO_NEXT: False,
        Status.SHOULD_PLAY_FORWARD: True,
        Status.SHOULD_RESET: False
    }

    graph_data = GraphData(tile_size, grid_size, None)
    # TODO: Have another button line-layer for reset and option
    raw_grid_data = initialize_gui(graph_data, status_dictionary)
    graph_data.graph = Graph(raw_grid_data, Shape2D.Type.RECTANGLE)

    path_processor = PathProcessor(
        status_dictionary,
        # TODO: Add slider for the speed (between 1 and 1000)
        update_frame_in_milliseconds=16,
        graph_data=graph_data)
    path_processor.process()

    TkinterSingleton.loop()
    path_processor.depth_first_search.kill_thread()
    path_processor.depth_first_search.join()

if __name__ == "__main__":
    main()

import random

from draw_sdk.tkinter_singleton import TkinterSingleton
from draw_sdk.colour import Colour

# TODO: There should be core and ai modules separately
from py_ai_sdk.core.dimensions import Dim2D
from py_ai_sdk.core.shapes import Shape2D
from py_ai_sdk.core.graph import Graph
from py_ai_sdk.algorithms.graph_search import GraphSearch

def create_grid(tile_size: Dim2D, grid_size: Dim2D):
    raw_data = []
    for y in range(grid_size.y):
        row_raw_data = []
        for x in range(grid_size.x):
            TkinterSingleton.create_frame_at(Dim2D(x, y), tile_size, Colour.BLACK)
            row_raw_data.append(0)
        raw_data.append(row_raw_data)
    return raw_data

def get_random_edge_point(grid_size):
    four_sides = ["top", "bottom", "left", "right"]
    chosen_side = four_sides[random.randint(0, len(four_sides) - 1)]
    return {
        "top": Dim2D(random.randint(0, grid_size.x - 1), 0),
        "bottom": Dim2D(random.randint(0, grid_size.x - 1), grid_size.y - 1),
        "left": Dim2D(0, random.randint(0, grid_size.y - 1)),
        "right": Dim2D(grid_size.x -1, random.randint(0, grid_size.y - 1))
    }[chosen_side]


def main():
    TkinterSingleton.start()

    tile_size = Dim2D(25, 25)
    grid_size = Dim2D(10, 10)
    raw_data = create_grid(tile_size, grid_size)

    graph = Graph(raw_data, Shape2D.Type.RECTANGLE)
    start_point = get_random_edge_point(grid_size)
    graph_search = GraphSearch(graph, start_point)
    neighbour_data = Graph.NeighbourData(Graph.NeighbourData.Type.CROSS, 1)
    paths = graph_search.depth_first_search(neighbour_data)

    def pop_path():
        TkinterSingleton.create_frame_at(paths.pop(0), tile_size, Colour.RED)
        if paths:
            TkinterSingleton.update(pop_path, 100)

    TkinterSingleton.update(pop_path, 100)

    TkinterSingleton.loop()

if __name__ == "__main__":
    main()

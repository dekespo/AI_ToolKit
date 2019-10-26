import unittest
from py_ai_sdk.templates.rectangle_world import example_1
from py_ai_sdk.core.search_algorithms import a_star_search, depth_first_search, breadth_first_search, dijkstra_search
from py_ai_sdk.core.dimensions import Dim2D
from py_ai_sdk.core.neighbours import get_available_neighbours2d_rectangle, get_neighbours2d_rectangle_4_sides
from py_ai_sdk.core.shapes import Rectangle

class SearchAlgorithmsTest(unittest.TestCase):
    def test_depth_first_search(self):
        graph, blocking_points = example_1()
        top_left_corner = Dim2D(0, 0)
        blocking_points = Dim2D.convert_candiates_to_dimensions(blocking_points)
        graph = Rectangle(top_left_corner, len(graph[0]), len(graph))
        start_point = Dim2D(0, 0)
        def get_neighbours_function(graph, current_position):
            return get_available_neighbours2d_rectangle(graph, blocking_points, get_neighbours2d_rectangle_4_sides, current_position)
        correct_path_list = Dim2D.convert_candiates_to_dimensions([
            (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
            (0, 7), (0, 8), (0, 9), (1, 9), (1, 8), (1, 7), (1, 6),
            (1, 5), (1, 4), (1, 3), (1, 2), (1, 1), (1, 0), (2, 0),
            (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
            (2, 8), (2, 9), (3, 9), (3, 8), (3, 7), (3, 6), (3, 5),
            (3, 4), (3, 3), (3, 2), (3, 1), (3, 0), (4, 5), (5, 5),
            (5, 4), (5, 3), (5, 2), (5, 1), (5, 0), (6, 0), (6, 1),
            (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8),
            (6, 9), (5, 9), (5, 8), (5, 7), (5, 6), (4, 9), (7, 9),
            (7, 8), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2),
            (7, 1), (7, 0), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4),
            (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (9, 9), (9, 8),
            (9, 7), (9, 6), (9, 5), (9, 4), (9, 3), (9, 2), (9, 1),
            (9, 0)
        ])
        self.assertEqual(depth_first_search(graph, start_point, get_neighbours_function), correct_path_list)

    def test_breadth_first_search(self):
        graph, blocking_points = example_1()
        top_left_corner = Dim2D(0, 0)
        blocking_points = Dim2D.convert_candiates_to_dimensions(blocking_points)
        graph = Rectangle(top_left_corner, len(graph[0]), len(graph))
        start_point = Dim2D(0, 0)
        def get_neighbours_function(graph, current_position):
            return get_available_neighbours2d_rectangle(graph, blocking_points, get_neighbours2d_rectangle_4_sides, current_position)
        correct_path_list = Dim2D.convert_candiates_to_dimensions([
            (0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2), (3, 0), (2, 1), (1, 2), (0, 3),
            (3, 1), (2, 2), (1, 3), (0, 4), (3, 2), (2, 3), (1, 4), (0, 5), (3, 3), (2, 4),
            (1, 5), (0, 6), (3, 4), (2, 5), (1, 6), (0, 7), (3, 5), (2, 6), (1, 7), (0, 8),
            (4, 5), (3, 6), (2, 7), (1, 8), (0, 9), (5, 5), (3, 7), (2, 8), (1, 9), (6, 5),
            (5, 6), (5, 4), (3, 8), (2, 9), (7, 5), (6, 6), (6, 4), (5, 7), (5, 3), (3, 9),
            (8, 5), (7, 6), (7, 4), (6, 7), (6, 3), (5, 8), (5, 2), (4, 9), (9, 5), (8, 6),
            (8, 4), (7, 7), (7, 3), (6, 8), (6, 2), (5, 9), (5, 1), (9, 6), (9, 4), (8, 7),
            (8, 3), (7, 8), (7, 2), (6, 9), (6, 1), (5, 0), (9, 7), (9, 3), (8, 8), (8, 2),
            (7, 9), (7, 1), (6, 0), (9, 8), (9, 2), (8, 9), (8, 1), (7, 0), (9, 9), (9, 1),
            (8, 0), (9, 0)
        ])
        self.assertEqual(breadth_first_search(graph, start_point, get_neighbours_function), correct_path_list)

    def test_dijkstra_search(self):
        graph, blocking_points = example_1()
        top_left_corner = Dim2D(0, 0)
        blocking_points = Dim2D.convert_candiates_to_dimensions(blocking_points)
        graph = Rectangle(top_left_corner, len(graph[0]), len(graph))
        start_point = Dim2D(0, 0)
        end_point = Dim2D(7, 6)
        def get_neighbours_function(graph, current_position):
            return get_available_neighbours2d_rectangle(graph, blocking_points, get_neighbours2d_rectangle_4_sides, current_position)
        correct_path_list = Dim2D.convert_candiates_to_dimensions([
            (0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (7, 6)
        ])
        self.assertEqual(dijkstra_search(graph, start_point, end_point, get_neighbours_function), correct_path_list)

    def test_a_star_search(self):
        graph, blocking_points = example_1()
        top_left_corner = Dim2D(0, 0)
        blocking_points = Dim2D.convert_candiates_to_dimensions(blocking_points)
        graph = Rectangle(top_left_corner, len(graph[0]), len(graph))
        start_point = Dim2D(0, 0)
        end_point = Dim2D(7, 6)
        heuristic_function = Dim2D.get_manathan_distance
        def get_neighbours_function(graph, current_position):
            return get_available_neighbours2d_rectangle(graph, blocking_points, get_neighbours2d_rectangle_4_sides, current_position)
        correct_path_list = Dim2D.convert_candiates_to_dimensions([
            (0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (7, 6)
        ])
        self.assertEqual(a_star_search(graph, start_point, end_point, heuristic_function, get_neighbours_function), correct_path_list)

if __name__ == "__main__":
    unittest.main()

import unittest

from py_ai_sdk.templates.rectangle_world import example_different_regions
from py_ai_sdk.algorithms.connected_component_labelling import ConnectedComponentLabelling
from py_ai_sdk.core.graph import Graph
from py_ai_sdk.core.shapes import Shape2D
from py_ai_sdk.core.dimensions import Dim2D

class ConnectedComponentLabellingTest(unittest.TestCase):

    def test_wiki_example(self):
        raw_data = example_different_regions()
        graph = Graph(raw_data, Shape2D.Type.RECTANGLE, blocking_values=[1])
        labeller = ConnectedComponentLabelling(graph)
        labeller.first_pass()
        first_pass_data = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 2, 2, 0, 0, 3, 3, 0, 0, 4, 4, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 3, 3, 3, 3, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 0, 0, 0, 3, 3, 3, 0, 0, 3, 3, 0],
            [0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 3, 3, 3, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 0, 0, 5, 3, 0, 0, 0, 3, 3, 0],
            [0, 0, 0, 0, 0, 0, 6, 6, 5, 3, 0, 0, 7, 3, 3, 3, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(labeller.get_labels_graph(), first_pass_data)
        labeller.second_pass()
        second_pass_data = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 4, 4, 0, 0, 4, 4, 0],
            [0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 4, 4, 4, 4, 0, 0],
            [0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 4, 4, 4, 4, 0, 0, 0],
            [0, 0, 2, 2, 2, 2, 0, 0, 0, 4, 4, 4, 0, 0, 4, 4, 0],
            [0, 2, 2, 2, 0, 0, 2, 2, 0, 0, 0, 4, 4, 4, 0, 0, 0],
            [0, 0, 2, 2, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 4, 4, 0],
            [0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 0, 0, 4, 4, 4, 4, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(labeller.get_labels_graph(), second_pass_data)
        regions = labeller.get_regions()
        self.assertEqual(len(regions), 3)
        self.assertTrue(Dim2D(0, 0) in regions[0])
        self.assertTrue(Dim2D(8, 3) in regions[0])
        self.assertTrue(Dim2D(11, 6) in regions[0])
        self.assertTrue(Dim2D(1, 2) in regions[2])
        self.assertTrue(Dim2D(4, 4) in regions[2])
        self.assertTrue(Dim2D(15, 1) in regions[4])
        self.assertTrue(Dim2D(13, 5) in regions[4])


if __name__ == "__main__":
    unittest.main()

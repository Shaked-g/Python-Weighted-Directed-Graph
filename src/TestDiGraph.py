from unittest import TestCase
from unittest import TestCase
from src.DiGraph import DiGraph
from src.NodeData import NodeData


class MyTestCase(TestCase):

    def setUp(self) -> None:
        # Generates a graph with 50 vertices and 98 edges
        self.graph = DiGraph()
        self.graph.add_node(0)  # 1
        for i in range(1, 50):
            self.graph.add_node(i)
            self.graph.add_edge(0, i, 10)
            self.graph.add_edge(i, 0, 20)

        pass

    def test_v_size(self):
        size = self.graph.v_size()
        self.assertEqual(size, 50)

    def test_e_size(self):
        edges_size = self.graph.e_size()
        # print(edges_size)
        self.assertEqual(edges_size, 98)

    def test_add_edge(self):
        # Trying to add an edge with nodes that dont exists
        self.assertFalse(self.graph.add_edge(-2, -3, 36))
        # Adding edge that already exists
        self.assertFalse(self.graph.add_edge(0, 1, 30))
        # Adding a new node and edge
        self.graph.add_node(60)
        self.graph.add_edge(60, 2, 2)

        edges_size = self.graph.e_size()
        self.assertEqual(edges_size, 99)

    def test_get_all_v(self):
        self.assertEqual(len(self.graph.get_all_v()), 50)

    def test_remove_edge(self):
        # Removes 1 edge from the graph
        self.graph.remove_edge(0, 1)
        edges_size = self.graph.e_size()

        self.assertEqual(edges_size, 97)

    def test_remove_node(self):
        size = self.graph.v_size()
        self.assertEqual(self.graph.v_size(), 50)
        self.graph.remove_node(4)
        self.graph.remove_node(22)
        size = self.graph.v_size()
        self.assertEqual(size, 48)

    def test_all_out_edges_of_node(self):
        self.assertTrue(len(self.graph.all_out_edges_of_node(0)) == self.graph.v_size() - 1)
        # tests the function after deleting node0 and all the edges of the graph
        self.graph.remove_node(0)
        self.assertEqual(self.graph.e_size(), 0)
        self.assertEqual(len(self.graph.all_out_edges_of_node(1)), 0)

    def test_all_in_edges_of_node(self):
        self.assertEqual(len(self.graph.all_in_edges_of_node(0)), 49)
        self.assertEqual(len(self.graph.all_in_edges_of_node(1)), 1)
        self.assertEqual(len(self.graph.all_in_edges_of_node(14)), 1)

    def test_get_mc(self):
        self.assertEqual(self.graph.get_mc(), 148)
        self.graph.add_node(100)
        self.assertEqual(self.graph.get_mc(), 149)
        self.graph.remove_node(100)
        self.assertEqual(self.graph.get_mc(), 150)
        self.graph.add_node(100)
        self.graph.add_edge(1, 100, 12)
        self.assertEqual(self.graph.get_mc(), 152)
        self.graph.remove_edge(1, 100)
        self.assertEqual(self.graph.get_mc(), 153)
        # removes node and 2 of his edges mc+3
        self.graph.remove_node(2)
        self.assertEqual(self.graph.get_mc(), 156)


if __name__ == '__main__':
    TestCase.main()

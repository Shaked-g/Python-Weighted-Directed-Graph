from unittest import TestCase
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class MyTestCase(TestCase):
    def setUp(self) -> None:
        # Generates a graph with 50 vertices and 98 edges
        graph = DiGraph()
        graph.add_node(0)  # 1
        for i in range(1, 50):
            graph.add_node(i)
            graph.add_edge(0, i, 10)
            graph.add_edge(i, 0, 20)
        self.graph_algo = GraphAlgo(graph=graph)

    def test_get_graph(self):
        # print(self.graph_algo.get_graph())
        # print(self.graph_algo.graph)
        self.assertEqual(self.graph_algo.get_graph(), self.graph_algo.graph)

    def test_save_to_json(self):
        self.assertTrue(self.graph_algo.save_to_json("json_test"))

    def test_load_from_json(self):
        g_algo = GraphAlgo()  # init an empty graph - for the GraphAlgo
        file = "../data/G_10_80_0.json"
        self.assertTrue((g_algo.load_from_json(file)))

    def test_shortest_path(self):
        # print(self.graph_algo.shortest_path(0, 3))
        self.assertEqual(self.graph_algo.shortest_path(1, 3), (30, [1, 0, 3]))
        self.assertEqual(self.graph_algo.shortest_path(0, 3), (10, [0, 3]))

    def test_connected_component(self):
        # print(self.graph_algo.connected_component(4))
        # print(list(range(0, 50)))
        self.assertEqual(self.graph_algo.connected_component(4), list(range(0, 50)))
        self.assertEqual(self.graph_algo.connected_component(25), list(range(0, 50)))
        # Invalid Inputs
        self.assertEqual(self.graph_algo.connected_component(60), [])
        self.assertEqual(self.graph_algo.connected_component(None), [])

    def test_connected_components(self):
        # print(self.graph_algo.connected_components())
        self.assertEqual(self.graph_algo.connected_components(), [list(range(0, 50))])
        g_algo = GraphAlgo()
        self.assertEqual(g_algo.connected_components(), [])


if __name__ == '__main__':
    TestCase.main()

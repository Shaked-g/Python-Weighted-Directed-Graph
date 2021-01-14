from src.GraphInterface import GraphInterface
from src.NodeData import NodeData


class DiGraph(GraphInterface):

    def __init__(self):
        self.Vertices = dict()
        self.Ni_in = dict()
        self.Ni_out = dict()
        self.__McCount = 0
        self.__EdgeSize = 0

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """
        # or use self.Vertices.keys
        return len(self.Vertices)

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        return self.__EdgeSize

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        return self.__McCount

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.

        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        if id1 not in self.Vertices or id2 not in self.Vertices or id2 in self.Ni_out[id1] or id1 in self.Ni_in[id2]:
            return False
        else:
            self.Ni_out[id1][id2] = weight
            self.Ni_in[id2][id1] = weight
            self.__McCount += 1
            self.__EdgeSize += 1
            return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.

        Note: if the node id already exists the node will not be added
        """
        if node_id not in self.Vertices:
            self.Vertices[node_id] = NodeData(key=node_id, pos=pos)
            self.Ni_in[node_id] = {}
            self.Ni_out[node_id] = {}
            self.__McCount += 1
            return True

        return False

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.

        Note: if the node id does not exists the function will do nothing
        """
        if node_id not in self.Vertices:
            return False
        else:
            for nib_out in self.all_out_edges_of_node(node_id).copy():
                # Sends all the edges going out a given node_id to remove func
                self.remove_edge(node_id, nib_out)
                self.remove_edge(nib_out, node_id)
            for nib_in in self.all_in_edges_of_node(node_id).copy():
                # Sends all the edges going in a given node_id to remove func
                self.remove_edge(node_id, nib_out)
                self.remove_edge(nib_out, node_id)
            # Deletes the node_id itself from records
            del self.Ni_in[node_id]
            del self.Ni_out[node_id]
            del self.Vertices[node_id]
            self.__McCount += 1
            return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.

        Note: If such an edge does not exists the function will do nothing
        """
        if node_id1 not in self.Ni_in[node_id2] or node_id2 not in self.Ni_out[node_id1]:
            return False
        else:
            del self.Ni_out[node_id1][node_id2]
            del self.Ni_in[node_id2][node_id1]
            self.__McCount += 1
            self.__EdgeSize -= 1
            return True

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph, each node is represented using a pair
         (node_id, node_data)
        """
        return self.Vertices

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)
         """
        return self.Ni_in[id1]

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
        (other_node_id, weight)
        """
        return self.Ni_out[id1]

    def __repr__(self):
        s = "Graph: |V|={} , |E|={} , MC={}\n".format(self.v_size(), self.__EdgeSize, self.__McCount)

        for nodes in self.Vertices.keys():
            s += "Node Number: {}".format(nodes)
            s += " |edges out| "
            s += str(len(self.all_out_edges_of_node(nodes)))
            s += " |edges in| "
            s += str(len(self.all_in_edges_of_node(nodes)))
            s += ","

        return s

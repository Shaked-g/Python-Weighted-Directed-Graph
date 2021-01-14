# Ariel_OOP_2020
## the Fourth Assignment in Java OOP course Overview:
This project represents an directional weighted graph and the uses of searching algorithms on it.<br>
The src folder contains two abstract classes , two classes which implements the abstract classes, two test classes<br>
And a node class and a main class named "Ex3_main"<br>

## NodeData:
NodeData is a class that implements the node object of the graph.<br>
With each node having a unique key, info, weight, tag and position in order to plot the graph. <br>

## DiGraph
`class DiGraph(GraphInterface):`
DiGraph is the class that implements the GraphInterface abstract class which represents a directional weighted graph.<br>
Every edge in the graph has a weight that represents the distance from another node and therefor it can only be bigger or equal to 0.<br>
<br>
Each Graph has:<br>
        `self.Vertices = dict()` {node_id : NodeData}<br>
        `self.Ni_in = dict()`  a nested dictonary with edges that go into a given node {node_id : { other_node_id : weight}}<br>
        `self.Ni_out = dict()`  a nested dictonary with edges that go out of a given node {node_id : { other_node_id : weight}}<br>
        `self.__McCount = 0` a Mode Change counter<br>
        `self.__EdgeSize = 0`an Edge Size counter<br><br>
        
The class has the following functions:<br>
    `def v_size(self) -> int:`  Returns the number of vertices in this graph<br>
    `def e_size(self) -> int:`  Returns the number of edges in this graph<br>
    `def get_mc(self) -> int:`  Returns the Mode Count for this graph<br>
    `def add_edge(self, id1: int, id2: int, weight: float) -> bool:`  <br>
    `def add_node(self, node_id: int, pos: tuple = None) -> bool:`<br>
    `def remove_node(self, node_id: int) -> bool:`<br>
    `def remove_edge(self, node_id1: int, node_id2: int) -> bool:`<br>
    `def get_all_v(self) -> dict:`  return a dictionary of all the nodes in the Graph (node_id, node_data)<br>
    `def all_in_edges_of_node(self, id1: int) -> dict:`  return a dictionary of all the nodes connected to (into) node_id -> (other_node_id, weight)<br>
    `def all_out_edges_of_node(self, id1: int) -> dict:`  return a dictionary of all the nodes connected from node_id -> (other_node_id, weight)<br>
   
## GraphAlgo:<br>
`class GraphAlgo(GraphAlgoInterface):`
GraphAlgo is a class that implements the GraphAlgoInterface abstract class and contains algorithms that can be used on a weighted directional graph.<br>
<br>
The class consists the methods:<br>
    `def get_graph(self) -> GraphInterface:`<br>
    `def load_from_json(self, file_name: str) -> bool:`<br>
    `def save_to_json(self, file_name: str) -> bool:`<br>
    `def shortest_path(self, id1: int, id2: int) -> (float, list):`  Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm<br>
    `def connected_component(self, id1: int) -> list:`  Finds the Strongly Connected Component(SCC) that node id1 is a part of.<br>
    `def connected_components(self) -> List[list]:`  Finds all the Strongly Connected Component(SCC) in the graph.<br>
    `def bfs(self, s: int, parm: bool) -> list:`  BFS implementation <br>
    `def plot_graph(self) -> None:`  Plots the graph.<br>

    

  







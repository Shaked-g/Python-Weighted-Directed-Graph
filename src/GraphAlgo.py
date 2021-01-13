import json
from typing import List
import heapq
import math

from src.DiGraph import DiGraph
from src import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self):
        self.graph = DiGraph()

    def get_graph(self) -> GraphInterface:
        """
        @return: the directed graph on which the algorithm works on.
        """
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name) as f:
                s = json.load(f)
                g = DiGraph()
            for node in s["Nodes"]:
                if "pos" in node:
                    pos = tuple(map(float, str(node["pos"]).split(",")))
                    g.add_node(key=node["id"], position=pos)
                else:
                    g.add_node(key=node["id"])

            for edge in s["Edges"]:
                g.add_edge(edge["src"], edge["dest"], edge["w"])
            self.graph = g
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            f.close()

    def save_to_json(self, file_name: str) -> bool:
        with open('../data/' + file_name, 'w', encoding='utf-8') as f:
            try:
                d = {"Nodes": [], "Edges": []}
                for src in self.graph.Ni_out.keys():
                    for dst, w in self.graph.all_out_edges_of_node(src).items():
                        d["Edges"].append({"src": src, "w": w, "dest": dst})

                for node in self.graph.V.values():
                    if node.position is not None:
                        d["Nodes"].append({"pos": str(node.position), "id": node.key})
                    else:
                        d["Nodes"].append({"id": node.key})
                json.dump(d, f, ensure_ascii=False, indent=4)
                return True
            except Exception as e:
                print("Error save to Json: " + e.__repr__())
                return False
            finally:
                f.close()

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through

        Notes:
        If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """
        unseen_nodes = self.graph.get_all_v()
        if id1 not in unseen_nodes or id2 not in unseen_nodes:
            return None

        track_predecessor = {id1: -1}
        shortest_distance = {}

        # Setting the Dist to infinity
        for node in unseen_nodes.keys():
            shortest_distance[node] = math.inf
        shortest_distance[id1] = 0

        q = []
        heapq.heappush(q, (0, id1))
        while q:
            v = heapq.heappop(q)[1]
            for u, w in self.graph.all_out_edges_of_node(v).items():
                if shortest_distance[u] > shortest_distance[v] + w:
                    shortest_distance[u] = shortest_distance[v] + w
                    track_predecessor[u] = v
                    heapq.heappush(q, (shortest_distance[u], u))
            if v == id2:
                break

        # Retrieving the path
        if shortest_distance[id2] == math.inf:
            return None
        path = []
        p = id2
        while p != -1:
            path.insert(0, p)
            p = track_predecessor[p]
        return shortest_distance[id2], path

    def connected_component(self, id1: int) -> list:
        pass

    def connected_components(self) -> List[list]:
        pass

    def plot_graph(self) -> None:
        pass

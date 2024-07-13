import sys

from Node import Node


class Graph:
    dict_for_graph = {}

    def __int__(self):
        self.dict_for_graph = {}
        self.size = 0

    def add_node(self, name: str) -> None:
        if name not in self.dict_for_graph:
            self.dict_for_graph[name] = Node(name)

    def get_node(self, name: str) -> Node:
        if name not in self.dict_for_graph:
            self.dict_for_graph[name] = Node(name)
        return self.dict_for_graph[name]

    def add_noaber_to(self, name: str, neighbor: str) -> None:
        self.add_node(neighbor)
        neighbor = self.dict_for_graph[neighbor]
        self.dict_for_graph[name].add_edge(neighbor)
        self.dict_for_graph[name].increment_edge(neighbor)

    def get_node_in_graph(self) -> set[str]:
        return set(self.dict_for_graph.keys())

    def print_graph(self) -> None:
        for node in self.dict_for_graph.values():
            print(node.name, " ")
            print("neighbor:", " ")
            print(node.edges)

    def print_stats(self) -> None:
        print("amount of visitied vertexes: " + str(Node.visit_vertex))
        print("amount of dieffrent vertexes visited: " + str(Node.new_vertexes))

        value = 0
        sum_value = 0
        for node in self.dict_for_graph.values():
            if node.curr_node_visitied != 0:
                value += 1
                sum_value += node.curr_node_visitied

        print("amount of visitied vertexes: " + str(sum_value))
        print("amount of dieffrent vertexes visited: " + str(value))

        size = 0
        size_cash = 0

        for key, value in self.dict_for_graph.items():
            size += value.size
            size_cash += value.size
            for key_2, value_2 in value.values.items():
                size_cash += sys.getsizeof(value_2)

        print(f"size of graph: {sys.getsizeof(self) + size_cash}"
              f", size of cash: {sys.getsizeof(self) - self.size + size_cash - size}, size no cash: {self.size + size}")


import random
import sys


class Node:
    current_wigth = 0.3
    next_wigth = 0.7
    visit_vertex = 0
    new_vertexes = 0

    def __init__(self, name: str):
        self.name = name
        self.edges = dict()
        self.neighbors_name = []
        self.values = {}
        self.cach = True
        self.curr_node_visitied = 0
        self.size = sys.getsizeof(self)

    def incres_value(self) -> None:
        pass
        # self.value += 1

    def add_edge(self, node, weight: int = 0) -> None:
        if node not in self.edges:
            self.edges[node] = weight

    def increment_edge(self, node) -> None:
        self.edges[node] += self.edges.get(node, 0) + 1

    def next_word(self) -> str:
        return random.choices(list(self.edges.keys()), weights=list(self.edges.values()))[0].name

    def get_max_wigth(self) -> int:
        if len(self.edges.values()) == 0:
            return 0
        return max(self.edges.values())

    def get_max_wigth_v2(self) -> int:
        weights = []
        for node in self.edges.keys():
            weights.append(self.edges[node] * 0.7 + node.get_max_wigth() * 0.3)

        return max(weights)

    def get_max_wigth_v3(self) -> int:
        weights = []
        for node in self.edges.keys():
            weights.append(self.edges[node] * 0.7 + node.get_max_wigth_v2() * 0.3)

        return max(weights)

    def get_max_wigth_virson_best(self, number_in_chane: int) -> int:
        # print(f"            In recurtion - level {number_in_chane}")
        Node.visit_vertex += 1
        self.curr_node_visitied += 1

        if number_in_chane in self.values and self.cach:
            return self.values[number_in_chane]

        if len(self.values.keys()) == 0:
            Node.new_vertexes += 1

        if number_in_chane == 0:
            value = self.get_max_wigth()
            if self.cach:
                self.values[number_in_chane] = value
            return value

        weights = []
        for node in self.edges.keys():
            weights.append(self.edges[node] * self.current_wigth +
                           node.get_max_wigth_virson_best(number_in_chane - 1) * self.next_wigth)

        if len(weights) == 0:
            if self.cach:
                self.values[number_in_chane] = 0
            return 0
        value = max(weights)
        if self.cach:
            self.values[number_in_chane] = value
        return value

    def next_word_v2(self) -> str:
        weights = []
        for node in self.edges.keys():
            weights.append(self.edges[node] * 0.8 + node.get_max_wigth() * 0.2)

        return random.choices(list(self.edges.keys()), weights=weights)[0].name

    def next_word_v3(self) -> str:
        weights = []
        for node in self.edges.keys():
            weights.append(self.edges[node] * 0.7 + node.get_max_wigth_v2() * 0.3)

        return random.choices(list(self.edges.keys()), weights=weights)[0].name

    def next_word_v4(self) -> str:
        weights = []
        for node in self.edges.keys():
            weights.append(self.edges[node] * 0.7 + node.get_max_wigth_v3() * 0.3)

        return random.choices(list(self.edges.keys()), weights=weights)[0].name

    def next_word_virson_best(self, number_in_chane: int = 10) -> str:
        Node.visit_vertex += 1
        self.curr_node_visitied += 1

        if (number_in_chane + 1) in self.values and self.cach:
            return random.choices(list(self.edges.keys()), weights=self.values[number_in_chane + 1])[0].name

        if len(self.values.keys()) == 0:
            Node.new_vertexes += 1

        weights = []
        size = len(self.edges.keys())
        for i, node in enumerate(self.edges.keys()):
            print(f"     getting next neighbor word's weight {i + 1}/{size}: got curr value: goinng into recursian")
            weights.append(self.edges[node] * self.current_wigth +
                           node.get_max_wigth_virson_best(number_in_chane) * self.next_wigth)

        if self.cach:
            self.values[number_in_chane + 1] = weights

        return random.choices(list(self.edges.keys()), weights=weights)[0].name

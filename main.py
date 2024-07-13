# This is a sample Python script.
import random
import string
import sys
import numpy as np

from graph import Graph


def go_over_a_file(file_name: str) -> list[str]:
    with open(file_name, 'r') as file:
        text = file.read()
        text = ' '.join(text.split())

        text = text.lower()

        text = text.translate(str.maketrans('', '', string.punctuation))

    fun_words = text.split()
    return fun_words


def compose(fun_g: Graph, fun_words: list[str], length: int = 50, recurtion_level: int = 2) -> list[str]:
    fun_composition = []
    fun_node = fun_g.get_node(random.choice(fun_words))
    fun_g.size = sys.getsizeof(fun_g)
    print(f"starting getting word with recurtion level of {recurtion_level}")
    print("=========================================================================")

    for i in range(length - 1):
        print(f"start with {i + 1}/{length}")
        fun_composition.append(fun_node.name)
        if len(fun_node.edges.keys()) == 0:
            fun_node = fun_g.get_node(random.choice(fun_words))
        else:
            fun_word = fun_node.next_word_virson_best(recurtion_level)
            fun_node = fun_g.get_node(fun_word)

        print(f"done with {i + 1}/{length}")
        print("---------------------------------------")

    print(f"start with {length}/{length}")
    fun_composition.append(fun_node.name)
    print(f"done with {length}/{length}")
    print("---------------------------------------")
    print("====================================================================")
    print("done all!!!")

    return fun_composition


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    n = np.array([[5,5,5], [0,0,0], [1,1,1]])
    print()

    words = go_over_a_file("herry.txt")
    g = Graph()

    g.add_node(words[0])
    prev_word = words[0]

    for word in words[1:]:
        g.add_node(word)
        g.add_noaber_to(prev_word, word)
        prev_word = word

    composition = compose(g, words, 10, 9)
    print(' '.join(composition))

    g.print_stats()

    # g.print_graph()

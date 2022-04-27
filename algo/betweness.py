import random

import networkx as nx
import matplotlib.pyplot as plt


def run(G):
    result = nx.betweenness_centrality(G, 100)
    max_ = max(result.values())
    for k, v in result.items():
        result[k] = v / max_
    print("start_draw")
    nodes = [k for k, v in sorted(result.items(), key=lambda x: x[1])[-4:]]
    new_graph = nx.Graph()
    for n in nodes:
        new_graph.add_node(n, color="#ff0000", size=900)
    for n in nodes:
        for k in G.neighbors(n):
            new_graph.add_edge(n, k)

    for n in list(new_graph.nodes()):
        if n not in nodes and len(list(new_graph.neighbors(n))) < 2:
            if random.random() > 0.1:
                new_graph.remove_node(n)

    nx.draw(new_graph)
    plt.show()

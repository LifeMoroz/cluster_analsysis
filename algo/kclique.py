from cdlib import algorithms
from networkx.algorithms.community import *

import networkx as nx
from matplotlib import pyplot as plt
from utils import draw


def run(G, k, small=False):
    result = algorithms.kclique(G, k)
    if small:
        cliq_com = next(k_clique_communities(G, k))

        sep_com = []
        for i in [9, 8, 7, 6, 5]:
            communities = k_clique_communities(G, i)
            for i in communities:
                if len(cliq_com & i) == 0:
                    sep_com.append(i)

        pos = nx.kamada_kawai_layout(G)

        plt.figure(figsize=(15, 15))
        nx.draw_networkx_edges(G, pos, alpha=0.3)
        all_nodes = nx.draw_networkx_nodes(G, pos, alpha=0.45, node_size=150)
        kcore_nodes = nx.draw_networkx_nodes(list(cliq_com), pos, nodelist=list(cliq_com), node_color="blue",
                                             node_size=300)
        kcore_nodes = nx.draw_networkx_nodes(list(sep_com[1]), pos, nodelist=list(sep_com[1]), node_color="green",
                                             node_size=300)
        kcore_nodes = nx.draw_networkx_nodes(list(sep_com[2]), pos, nodelist=list(sep_com[2]), node_color="black",
                                             node_size=300)

        # kcore_nodes = nx.draw_networkx_nodes(cliq_com[8], pos, nodelist=cliq_com[8], node_color="yellow",node_size=300)

        plt.title('K-clique communities', size=15)
        plt.axis('off')
        plt.show()
    else:
        draw(G, result.communities)

from cdlib import algorithms

from utils import draw


def run(G, k):
    result = algorithms.kclique(G, k)
    draw(G, result.communities)

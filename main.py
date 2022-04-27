import click
import networkx as nx

import algo.eigenvector
import algo.greedy
import algo.kclique
import algo.label_propagation
import algo.spectral_clustering
import algo.walktrap


def get_graph(data):
    G = nx.Graph()

    with open(data) as f:
        f.readline()
        for ids in f:
            G.add_edge(*ids.strip().split(","))
    return G


@click.command("greedy")
@click.option("--file", default=".data/musae_facebook_edges_1.csv")
def greedy(file):
    algo.greedy.run(get_graph(file))


@click.command("eigenvector")
@click.option("--file", default=".data/musae_facebook_edges_1.csv")
def eigenvector(file):
    algo.eigenvector.run(get_graph(file))


@click.command("kclique")
@click.option("--file", default=".data/musae_facebook_edges_1.csv")
@click.option("--k", default=10)
def kclique(file, k):
    algo.kclique.run(get_graph(file), k)


@click.command("label_propagation")
@click.option("--file", default=".data/musae_facebook_edges_1.csv")
def label_propagation(file):
    algo.label_propagation.run(get_graph(file))


@click.command("spectral_clustering")
@click.option("--file", default=".data/musae_facebook_edges_1.csv")
@click.option("--kmax", default=10)
def spectral_clustering(file, kmax):
    algo.spectral_clustering.run(get_graph(file), kmax)


@click.command("walktrap")
@click.option("--file", default=".data/musae_facebook_edges_1.csv")
def walktrap(file):
    algo.walktrap.run(get_graph(file))


@click.group()
def cli():
    pass


cli.add_command(greedy)
cli.add_command(eigenvector)
cli.add_command(kclique)
cli.add_command(label_propagation)
cli.add_command(spectral_clustering)
cli.add_command(walktrap)


if __name__ == "__main__":
    cli()

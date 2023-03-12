import networkx as nx
import matplotlib.pyplot as plt


def draw(dots=None, edges=None):
    graph = nx.Graph()
    graph.add_edges_from([("A", "B"), ("A", "C"), ("C", "B")])
    pos = nx.spring_layout(graph)
    nx.draw_networkx(graph, pos, node_size=500)
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_edges(graph, pos)
    plt.show()

from Task import Task
from datetime import datetime
import random, math, argparse
import numpy as np
from numpy.random.mtrand import sample
from matplotlib import pyplot as plt

# import networkx as nx
# from matplotlib import pyplot as plt


class TaskGenerator:
    def __init__(num_tasks=25, workflow_type=None) -> None:
        num_tasks = num_tasks
        workflow_type = workflow_type
        task_list: dict = None
        max_end_point = None
        beta = None


# def draw_dags():
#     graph = nx.Graph()s
#     graph.add_edges_from([("m", "p"), ("n", "p"), ("o", "p"), ("p", "q")])
#     nx.is_directed(graph)  # => False
#     nx.is_directed_acyclic_graph(graph)  #
#     plt.tight_layout()
#     return


# draw_dags()

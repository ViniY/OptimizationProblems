from Task import Task
from datetime import datetime
import random, math, argparse
import numpy as np
from numpy import random
from numpy.random.mtrand import sample

# from matplotlib import pyplot as plt
import json
import sys


import networkx as nx

from matplotlib import pyplot as plt


class DAGGenerator:
    def __init__(self, **args) -> None:
        # Here defines the pattern of the workflow
        self.num_tasks = args.get("num_tasks", 25)
        self.workflow_type = args.get("workflow_type", None)
        self.task_list: dict = args.get("task_list", [])
        self.max_end_point = args.get("max_end_point", 1)
        self.alpha = args.get("alpha", 1)  # Define the deepness of the workflow
        self.beta = args.get("beta", 1.0)  # Define the number of task within each layer
        self.variation = args.get(
            "variation", 0.0
        )  # if there is any variation of the number of the tasks

    def _DAG_generation_(self):

        return


# def draw_dags():
#     graph = nx.Graph()s
#     graph.add_edges_from([("m", "p"), ("n", "p"), ("o", "p"), ("p", "q")])
#     nx.is_directed(graph)  # => False
#     nx.is_directed_acyclic_graph(graph)  #
#     plt.tight_layout()
#     return


# draw_dags()


class TaskGenerator:
    def __init__(self, parent_task, **args) -> None:
        self.mean_task_size = args.get("avg_task_size", 200)
        self.std_task_size = args.get("std_task_size", 0.2)
        self.disk_req_mean = args.get("disk_req", None)
        self.memory_req_mean = args.get("memory_req", None)
        self.disk_req_std = args.get("disk_req_std", None)
        self.memory_req_std = args.get("memory_req_std", None)
        self.dttm = None

    def _generate_task_(self):
        task_size = random.normal(loc=self.mean_task_size, scale=self.std_task_size)
        if self.disk_req_mean and self.disk_req_stds:
            disk_req = random.normal(loc=self.disk_req_mean, scale=self.disk_req_std)
        else:
            disk_req = self.disk_req_mean
        if self.memory_req_mean and self.memory_req_std:
            memory_req = random.normal(
                loc=self.memory_req_mean, scale=self.memory_req_std
            )
        else:
            memory_req = self.memory_req_mean

        new_task = Task(
            datetime.now(),
            task_size=task_size,
            sla=None,
            memory_req=memory_req,
            disk_req=disk_req,
            depend_on=[],
        )

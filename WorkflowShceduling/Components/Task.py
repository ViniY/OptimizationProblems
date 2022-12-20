import os
import sys
from datetime import datetime, timezone


class Task:
    def __init__(self) -> None:
        self.task_id: str = None
        self.dttm = None  # crated time
        self.task_size = None
        self.memory_req = None
        self.disk_req = None
        self.sla = None
        self.depend_on = []
        self.start_time = None
        self.finish_time = None
        self.in_progress = False

    def _set_parent_(self, parent_task):
        self.depend_on.append(parent_task)

    # def _remove_dependency_(self, to_remove):

    def _update_task_size_(self, task_size):
        self.task_size = task_size

    def _update_finish_time_(self, finish_time):
        self.finish_time = finish_time

    def _update_sla_(self, new_sla):
        self.sla = new_sla

    def process_start(self, time):
        self.start_time = time
        self.in_progress = True

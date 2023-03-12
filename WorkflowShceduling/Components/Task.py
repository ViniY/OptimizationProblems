import os
import sys
from datetime import datetime, timezone
import logging
from uuid import uuid4


class Task:
    def __init__(
        self,
        dttm,
        task_size,
        sla,
        memory_req=None,
        disk_req=None,
        depend_on=[],
    ) -> None:
        # task features need to be predefined
        self.task_id = uuid4()
        self.dttm = dttm  # created time
        self.task_size = task_size
        self.memory_req = memory_req
        self.disk_req = disk_req
        self.sla = sla
        self.depend_on = depend_on
        # attribute during and after processing
        self.start_time = None
        self.finish_time = None
        self.status = "Waiting"
        self.execution_time = None
        self.total_time = None
        self.wait_time = None
        # Relationship
        self.parent_task = None
        self.children_tasks = []
        self.deepth = None  # Can be used for algorithm verifications

    def _set_parent_(self, parent_task):
        if self.status == "running":
            logging.warning("Invalid Actions : !!!!")
            logging.warning("Task is in progress")
        else:
            self.depend_on.append(parent_task)

    # def _remove_dependency_(self, to_remove):
    def _update_task_size_(self, task_size):
        if self.status == "running":
            logging.warning("Invalid Actions : Job is running currently!!!!")
            logging.warning("Task is in progress")
        else:
            self.task_size = task_size

    def _update_finish_time_(self, finish_time):
        self.finish_time = finish_time

    def _update_sla_(self, new_sla):
        self.sla = new_sla

    def _update_memory_req_(self, new_memory_req):
        self.memory_req = new_memory_req

    def _update_disk_req_(self, new_disk_req):
        self.disk_req = new_disk_req

    def _process_start_(self, time):
        self.start_time = time
        self.in_progress = "running"
        self.wait_time = self.start_time - self.dttm

    def _task_end_(self, time):
        self.finish_time = time
        self.in_progress = "success"
        self.execution_time = self.finish_time - self.start_time
        self.total_time = self.execution_time + self.wait_time

    def _stop_tasK_(self, time):
        if self.status == "running":
            logging.warning(
                " The task {}, is stopped and the execution time is recorded".format(
                    self.task_id
                )
            )

            self.execution_time = time - self.start_time
            self.status = "stopped"
            return

        if self.status == "waiting":
            logging.warning(
                "The task {} is currently waiting and will be removed".format(
                    self.task_id
                )
            )
            return

        if self.status == "success":
            logging.warning(
                " The task {} is already succeed no actions will be made".format(
                    self.task_id
                )
            )
            return

        logging.warning("Invalid Action on Task {}".format(self.task_id))

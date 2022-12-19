import os
import sys
from datetime import datetime, timezone


class Task:
    def __init__(self) -> None:
        task_id: str = None
        dttm = None
        task_size = None
        memory_req = None
        disk_req = None
        sla = None
        depend_on = []

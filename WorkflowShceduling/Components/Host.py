from VM import VM
from PE import PE
from typing import List


class Host:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(
        self, id, RAM_Provisioner, BW_Provisioner, storage, VM_Scheduler, PE_list
    ) -> None:
        id = id
        storage = storage
        RAM_Provisioner = RAM_Provisioner
        BW_Provisioner = BW_Provisioner
        VM_Scheduler = VM_Scheduler
        VM_list: List[VM] = None
        # PE representing the processing elements (cores) which defines the processing capability.
        PE_list: List[PE] = PE_list
        failed: bool = None
        location = None

# deletes the given task ID. Returns (True, deleted_task) or (False, reason)
from typing import Tuple, Dict, List
from .helpers import find_task_index_by_id

def delete_task(tasks: List[Dict], task_id: int) -> Tuple[bool, object]:
    idx = find_task_index_by_id(tasks, task_id)
    if idx == -1:
        return False, f"Task with id {task_id} not found."
    deleted = tasks.pop(idx)
    # Note: We don't reshuffle IDs; generate_id will skip used IDs but will reuse freed IDs if smallest.
    return True, deleted

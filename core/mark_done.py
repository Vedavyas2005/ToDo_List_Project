# sets status to 'Done' for the specified task
# returns (True, updated_task) or (False, reason)

from typing import Tuple, Dict, List
from .helpers import find_task_index_by_id
from .helpers import current_timestamp

def mark_done(tasks: List[Dict], task_id: int) -> Tuple[bool, object]:
    idx = find_task_index_by_id(tasks, task_id)
    if idx == -1:
        return False, f"Task with id {task_id} not found."
    task = tasks[idx]
    if task.get("status") == "Done":
        return False, f"Task {task_id} is already marked Done."
    task["status"] = "Done"
    task["last_updated"] = current_timestamp()
    tasks[idx] = task
    return True, task.copy()

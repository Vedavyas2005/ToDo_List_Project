"""
update_task has the following: (tasks, task_id, *, new_description=None, priority=None, category=None, notes=None)
Updates provided fields for a task. Returns (True, updated_task) or (False, reason)
"""
from typing import Tuple, Dict, List, Optional
from .helpers import find_task_index_by_id, current_timestamp

def update_task(tasks: List[Dict], task_id: int,
                *,
                new_description: Optional[str] = None,
                priority: Optional[str] = None,
                category: Optional[str] = None,
                notes: Optional[str] = None) -> Tuple[bool, object]:
    idx = find_task_index_by_id(tasks, task_id)
    if idx == -1:
        return False, f"Task with id {task_id} not found."

    task = tasks[idx]
    changed = False

    if new_description is not None:
        if not new_description.strip():
            return False, "Task description cannot be empty."
        task["task"] = new_description.strip()
        changed = True

    if priority is not None:
        task["priority"] = priority
        changed = True

    if category is not None:
        task["category"] = category
        changed = True

    if notes is not None:
        task["notes"] = notes
        changed = True

    if changed:
        task["last_updated"] = current_timestamp()
        tasks[idx] = task
        return True, task.copy()
    else:
        return False, "No changes provided."

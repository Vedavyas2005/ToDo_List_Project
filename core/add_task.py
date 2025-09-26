 #add_task(tasks, description, *, priority=None, category=None, notes=None)
from typing import Tuple, Dict, List, Optional
from .helpers import generate_id, current_timestamp
from .data_model import MAX_TASKS

def add_task(tasks: List[Dict], description: str,
             priority: Optional[str] = None,
             category: Optional[str] = None,
             notes: Optional[str] = None) -> Tuple[bool, object]:
    if not isinstance(description, str) or not description.strip():
        return False, "Task description cannot be empty."

    if len(tasks) >= MAX_TASKS:
        return False, f"Task limit reached ({MAX_TASKS}). Delete an existing task before adding."
    # Here we dynamically create a new task in the form of a dict
    new_task = {
        "id": generate_id(tasks),
        "task": description.strip(),
        "status": "Pending",
        "created_on": current_timestamp(),
    }
    # Optional fields
    if priority:
        new_task["priority"] = priority
    if category:
        new_task["category"] = category
    if notes:
        new_task["notes"] = notes

    tasks.append(new_task)
    return True, new_task

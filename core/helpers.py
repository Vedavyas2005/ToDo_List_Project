from datetime import datetime
from typing import List, Dict

def current_timestamp() -> str:
    # returnss ISO-like timestamp string
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def generate_id(tasks: List[Dict]) -> int:
    # generate a new unique ID for a task based on existing tasks
    # always returns a positive integer not used in tasks
    existing_ids = {t["id"] for t in tasks if "id" in t}
    new_id = 1
    while new_id in existing_ids:
        new_id += 1
    return new_id

def find_task_index_by_id(tasks: List[Dict], tid: int) -> int:
    # return index of task with id == tid, or -1 if not found!!
    for idx, t in enumerate(tasks):
        if t.get("id") == tid:
            return idx
    return -1

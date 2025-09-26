from typing import List, Dict

# max tasks allowed 
MAX_TASKS: int = 8


# We are not defining the schema as python can take dynamic dictionaries and i am defining dictionaries in other files dynamically
# id (int), task (str), status (str), created_on (str), priority (str, optional), category (str, optional), notes (str, optional)
tasks: List[Dict] = []

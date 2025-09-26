from typing import List, Dict, Optional

def view_tasks(tasks: List[Dict], *,
               filter_status: Optional[str] = None,
               search_keyword: Optional[str] = None) -> List[Dict]:
    results = []
    for t in tasks:
        # filters by status if provided
        if filter_status and t.get("status", "").strip().title() != filter_status.strip().title():
            continue

        # searches keyword in task title or notes
        if search_keyword:
            kw = search_keyword.lower()
            in_title = kw in t.get("task", "").lower()
            in_notes = kw in t.get("notes", "").lower() if t.get("notes") else False
            if not (in_title or in_notes):
                continue

        results.append(t.copy())
    return results
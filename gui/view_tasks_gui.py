# this is View Tasks panel: displays tasks in a table-like list with simple sorting and filtering
import customtkinter as ctk
from core.view_tasks import view_tasks
from tkinter import messagebox

class ViewTasksPanel(ctk.CTkFrame):
    def __init__(self, master, tasks_ref, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.tasks_ref = tasks_ref
        self._build_ui()

    def _build_ui(self):
        self.grid_columnconfigure(0, weight=1)
        title = ctk.CTkLabel(self, text="Tasks", font=(None, 18, "bold"))
        title.grid(row=0, column=0, sticky="w", padx=12, pady=(8,12))

        # Controls
        ctrl_frame = ctk.CTkFrame(self)
        ctrl_frame.grid(row=1, column=0, sticky="ew", padx=12, pady=6)
        ctrl_frame.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(ctrl_frame, text="Filter:").grid(row=0, column=0, padx=6)
        self.filter_cb = ctk.CTkComboBox(ctrl_frame, values=["All", "Pending", "In Progress", "Done"])
        self.filter_cb.set("All")
        self.filter_cb.grid(row=0, column=1, padx=6, sticky="w")

        ctk.CTkLabel(ctrl_frame, text="Search:").grid(row=0, column=2, padx=6)
        self.search_entry = ctk.CTkEntry(ctrl_frame, placeholder_text="Keyword")
        self.search_entry.grid(row=0, column=3, padx=6, sticky="ew")

        refresh_btn = ctk.CTkButton(ctrl_frame, text="Refresh", command=self.refresh)
        refresh_btn.grid(row=0, column=4, padx=6)

        # Listbox-like display
        self.listbox = ctk.CTkTextbox(self, height=260, state="disabled")
        self.listbox.grid(row=2, column=0, sticky="nsew", padx=12, pady=8)

        # initial populate
        self.refresh()

    def refresh(self):
        filt = self.filter_cb.get().strip()
        if filt == "All":
            filt = None
        """if filt:
            filt = filt.strip().title()"""
        search = self.search_entry.get().strip() or None
        items = view_tasks(self.tasks_ref, filter_status=filt, search_keyword=search)

        self.listbox.configure(state="normal")
        self.listbox.delete("1.0", "end")
        if not items:
            self.listbox.insert("end", "No tasks available.\n")
        else:
            pending = sum(1 for t in items if t.get("status") != "Done")
            done = sum(1 for t in items if t.get("status") == "Done")
            self.listbox.insert("end", f"Total: {len(items)}   Pending: {pending}   Done: {done}\n")
            self.listbox.insert("end", "-"*60 + "\n")
            for t in items:
                lines = [
                    f"ID: {t['id']}  •  {t['task']}",
                    f"    Status: {t.get('status','Pending')}  |  Priority: {t.get('priority','-')}  |  Category: {t.get('category','-')}",
                    f"    Created: {t.get('created_on','-')}" + (f"  |  Updated: {t.get('last_updated')}" if t.get('last_updated') else ""),
                ]
                if t.get("notes"):
                    lines.append(f"    Notes: {t['notes']}")
                self.listbox.insert("end", "\n".join(lines) + "\n\n")
        self.listbox.configure(state="disabled")

import customtkinter as ctk
from tkinter import messagebox
from core.update_task import update_task
from core.helpers import find_task_index_by_id

class UpdateTaskPanel(ctk.CTkFrame):
    def __init__(self, master, tasks_ref, refresh_callback=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.tasks_ref = tasks_ref
        self.refresh_callback = refresh_callback
        self._build_ui()

    def _build_ui(self):
        self.grid_columnconfigure(1, weight=1)
        ctk.CTkLabel(self, text="Update Task", font=(None, 18, "bold")).grid(row=0, column=0, columnspan=2, pady=(8,12))

        ctk.CTkLabel(self, text="Task ID:").grid(row=1, column=0, padx=8, pady=6, sticky="w")
        self.id_entry = ctk.CTkEntry(self)
        self.id_entry.grid(row=1, column=1, padx=8, pady=6, sticky="ew")

        ctk.CTkButton(self, text="Load", command=self._load_current).grid(row=1, column=2, padx=8, pady=6)

        ctk.CTkLabel(self, text="New Description:").grid(row=2, column=0, padx=8, pady=6, sticky="w")
        self.new_desc = ctk.CTkEntry(self)
        self.new_desc.grid(row=2, column=1, padx=8, pady=6, sticky="ew")

        ctk.CTkLabel(self, text="Priority:").grid(row=3, column=0, padx=8, pady=6, sticky="w")
        self.priority = ctk.CTkComboBox(self, values=["", "High", "Medium", "Low"])
        self.priority.set("")
        self.priority.grid(row=3, column=1, padx=8, pady=6, sticky="w")

        ctk.CTkLabel(self, text="Category:").grid(row=4, column=0, padx=8, pady=6, sticky="w")
        self.category = ctk.CTkEntry(self)
        self.category.grid(row=4, column=1, padx=8, pady=6, sticky="ew")

        ctk.CTkLabel(self, text="Notes:").grid(row=5, column=0, padx=8, pady=6, sticky="nw")
        self.notes = ctk.CTkTextbox(self, height=80)
        self.notes.grid(row=5, column=1, padx=8, pady=6, sticky="ew")

        ctk.CTkButton(self, text="Update", command=self._on_update).grid(row=6, column=0, columnspan=3, pady=12, padx=8, sticky="ew")

    def _load_current(self):
        try:
            tid = int(self.id_entry.get().strip())
        except Exception:
            messagebox.showwarning("Invalid", "Enter a valid numeric Task ID.")
            return
        idx = find_task_index_by_id(self.tasks_ref, tid)
        if idx == -1:
            messagebox.showwarning("Not found", f"Task {tid} not found.")
            return
        t = self.tasks_ref[idx]
        self.new_desc.delete(0, "end")
        self.new_desc.insert(0, t.get("task",""))
        self.priority.set(t.get("priority",""))
        self.category.delete(0, "end")
        self.category.insert(0, t.get("category",""))
        self.notes.delete("1.0", "end")
        if t.get("notes"):
            self.notes.insert("1.0", t.get("notes"))

    def _on_update(self):
        try:
            tid = int(self.id_entry.get().strip())
        except Exception:
            messagebox.showwarning("Invalid", "Enter a valid numeric Task ID.")
            return

        new_desc = self.new_desc.get().strip() or None
        prio = self.priority.get().strip() or None
        cat = self.category.get().strip() or None
        notes = self.notes.get("1.0", "end").strip() or None

        ok, res = update_task(self.tasks_ref, tid, new_description=new_desc, priority=prio, category=cat, notes=notes)
        if ok:
            messagebox.showinfo("Updated", f"Task {tid} updated.")
            if self.refresh_callback:
                self.refresh_callback()
        else:
            messagebox.showwarning("Could not update", res)

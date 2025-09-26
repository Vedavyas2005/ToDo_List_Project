# this file/module collects user input and calls core.add_task
# gui/add_task_gui.py
import customtkinter as ctk
from tkinter import messagebox
from core.add_task import add_task

class AddTaskPanel(ctk.CTkFrame):
    def __init__(self, master, tasks_ref, refresh_callback=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.tasks_ref = tasks_ref
        self.refresh_callback = refresh_callback
        self._build_ui()

    def _build_ui(self):
        theme = self.winfo_toplevel()._app_theme 
        self.grid_columnconfigure(1, weight=1)
        title = ctk.CTkLabel(self, text="Add New Task", font=(None, 18, "bold"))
        title.grid(row=0, column=0, columnspan=2, pady=(10,16))

        ctk.CTkLabel(self, text="Task:").grid(row=1, column=0, sticky="w", padx=8, pady=6)
        self.entry_task = ctk.CTkEntry(self, placeholder_text="Enter task title", width=400)
        self.entry_task.grid(row=1, column=1, sticky="ew", padx=8, pady=6)

        ctk.CTkLabel(self, text="Priority:").grid(row=2, column=0, sticky="w", padx=8, pady=6)
        self.priority = ctk.CTkComboBox(self, values=["High", "Medium", "Low"], width=200)
        self.priority.set("Medium")
        self.priority.grid(row=2, column=1, sticky="w", padx=8, pady=6)

        ctk.CTkLabel(self, text="Category:").grid(row=3, column=0, sticky="w", padx=8, pady=6)
        self.category = ctk.CTkEntry(self, placeholder_text="Work / Personal / Study", width=200)
        self.category.grid(row=3, column=1, sticky="w", padx=8, pady=6)

        ctk.CTkLabel(self, text="Notes (optional):").grid(row=4, column=0, sticky="nw", padx=8, pady=6)
        self.notes = ctk.CTkTextbox(self, height=80)
        self.notes.grid(row=4, column=1, sticky="ew", padx=8, pady=6)

        add_btn = ctk.CTkButton(self, text="Add Task", command=self._on_add,
                                fg_color=theme["accent"], hover_color=theme["accent_hover"])
        add_btn.grid(row=5, column=0, columnspan=2, pady=12, padx=12, sticky="ew")

    def _on_add(self):
        desc = self.entry_task.get().strip()
        prio = self.priority.get().strip() or None
        cat = self.category.get().strip() or None
        notes = self.notes.get("1.0", "end").strip() or None

        ok, result = add_task(self.tasks_ref, desc, priority=prio, category=cat, notes=notes)
        if ok:
            messagebox.showinfo("Success", f"Task added: {result['task']}")
            self.entry_task.delete(0, "end")
            self.category.delete(0, "end")
            self.notes.delete("1.0", "end")
            if self.refresh_callback:
                self.refresh_callback()
        else:
            messagebox.showwarning("Could not add task", result)
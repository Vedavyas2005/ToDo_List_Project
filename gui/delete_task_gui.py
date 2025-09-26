# delete task panel with confirmation.
import customtkinter as ctk
from tkinter import messagebox
from core.delete_task import delete_task

class DeleteTaskPanel(ctk.CTkFrame):
    def __init__(self, master, tasks_ref, refresh_callback=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.tasks_ref = tasks_ref
        self.refresh_callback = refresh_callback
        self._build_ui()

    def _build_ui(self):
        ctk.CTkLabel(self, text="Delete Task", font=(None, 18, "bold")).grid(row=0, column=0, pady=(8,12), padx=8)
        ctk.CTkLabel(self, text="Task ID to delete:").grid(row=1, column=0, sticky="w", padx=8)
        self.id_entry = ctk.CTkEntry(self)
        self.id_entry.grid(row=2, column=0, sticky="ew", padx=8, pady=6)
        ctk.CTkButton(self, text="Delete", command=self._on_delete).grid(row=3, column=0, pady=10, padx=8, sticky="ew")

    def _on_delete(self):
        try:
            tid = int(self.id_entry.get().strip())
        except Exception:
            messagebox.showwarning("Invalid", "Enter a valid numeric Task ID.")
            return
        confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete task {tid}?")
        if not confirm:
            return
        ok, res = delete_task(self.tasks_ref, tid)
        if ok:
            messagebox.showinfo("Deleted", f"Task {tid} deleted.")
            if self.refresh_callback:
                self.refresh_callback()
        else:
            messagebox.showwarning("Could not delete", res)

# panel to mark tasks as Done
# accepts single or comma-separated IDs to mark multiple tasks

import customtkinter as ctk
from tkinter import messagebox
from core.mark_done import mark_done

class MarkDonePanel(ctk.CTkFrame):
    def __init__(self, master, tasks_ref, refresh_callback=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.tasks_ref = tasks_ref
        self.refresh_callback = refresh_callback
        self._build_ui()

    def _build_ui(self):
        ctk.CTkLabel(self, text="Mark Task(s) Done", font=(None, 18, "bold")).grid(row=0, column=0, pady=(8,12), padx=8)
        ctk.CTkLabel(self, text="Enter ID(s) (comma separated):").grid(row=1, column=0, sticky="w", padx=8)
        self.ids_entry = ctk.CTkEntry(self)
        self.ids_entry.grid(row=2, column=0, sticky="ew", padx=8, pady=6)
        ctk.CTkButton(self, text="Mark Done", command=self._on_mark).grid(row=3, column=0, pady=10, padx=8, sticky="ew")

    def _on_mark(self):
        s = self.ids_entry.get().strip()
        if not s:
            messagebox.showwarning("Input required", "Please enter at least one task ID.")
            return
        id_list = []
        for part in s.split(","):
            try:
                id_list.append(int(part.strip()))
            except Exception:
                messagebox.showwarning("Invalid", f"Invalid ID '{part.strip()}'. Use numbers separated by commas.")
                return
        messages = []
        for tid in id_list:
            ok, res = mark_done(self.tasks_ref, tid)
            if ok:
                messages.append(f"[{tid}] Done")
            else:
                messages.append(f"[{tid}] Error: {res}")
        messagebox.showinfo("Result", "\n".join(messages))
        if self.refresh_callback:
            self.refresh_callback()

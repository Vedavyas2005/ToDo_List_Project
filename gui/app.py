# this is the main GUI application - ties menu and panels together
# this module/file implements theme toggle and DPI handling
import customtkinter as ctk
import tkinter as tk
from gui.themes import apply_theme, THEMES
from gui.menu_gui import MenuPanel
from gui.add_task_gui import AddTaskPanel
from gui.view_tasks_gui import ViewTasksPanel
from gui.update_task_gui import UpdateTaskPanel
from gui.mark_done_gui import MarkDonePanel
from gui.delete_task_gui import DeleteTaskPanel
from core.data_model import tasks

class ToDoApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("To-Do List App")
        # DPI handling & scaling - keep UI crisp and not too large
        try:
            # attempt to use system DPI scaling (may vary by platform)
            self.tk.call('tk', 'scaling', 1.0)
        except Exception:
            pass

        # Start with dark theme by default
        self._theme_name = "dark"
        apply_theme(self, self._theme_name)

        # window geometry
        self.geometry("900x560")
        self.minsize(800, 480)

        # layout: left menu + right content
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Menu
        self.menu_panel = MenuPanel(self,
                                   on_add=self.show_add,
                                   on_view=self.show_view,
                                   on_update=self.show_update,
                                   on_mark_done=self.show_mark_done,
                                   on_delete=self.show_delete,
                                   on_toggle_theme=self.toggle_theme)
        self.menu_panel.grid(row=0, column=0, sticky="nsw", padx=10, pady=10)

        # Content area
        self.content_frame = ctk.CTkFrame(self)
        self.content_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_rowconfigure(0, weight=1)

        # panels (instantiate but don't grid them until needed)
        self.panels = {}
        self._init_panels()
        self.show_view()  # show default

    def _init_panels(self):
        # note: each panel gets reference to global tasks list
        self.panels["add"] = AddTaskPanel(self.content_frame, tasks_ref=tasks, refresh_callback=self._refresh_view)
        self.panels["view"] = ViewTasksPanel(self.content_frame, tasks_ref=tasks)
        self.panels["update"] = UpdateTaskPanel(self.content_frame, tasks_ref=tasks, refresh_callback=self._refresh_view)
        self.panels["mark_done"] = MarkDonePanel(self.content_frame, tasks_ref=tasks, refresh_callback=self._refresh_view)
        self.panels["delete"] = DeleteTaskPanel(self.content_frame, tasks_ref=tasks, refresh_callback=self._refresh_view)

    def _hide_all_panels(self):
        for p in self.panels.values():
            p.grid_forget()

    def _show_panel(self, key):
        self._hide_all_panels()
        panel = self.panels.get(key)
        if panel:
            panel.grid(row=0, column=0, sticky="nsew")

    def show_add(self):
        self._show_panel("add")

    def show_view(self):
        self._show_panel("view")
        # ensure view panel refreshes when shown
        self._refresh_view()

    def show_update(self):
        self._show_panel("update")

    def show_mark_done(self):
        self._show_panel("mark_done")

    def show_delete(self):
        self._show_panel("delete")

    def _refresh_view(self):
        view_panel = self.panels.get("view")
        if view_panel:
            view_panel.refresh()

    def toggle_theme(self):
        # swap theme
        self._theme_name = "light" if self._theme_name == "dark" else "dark"
        apply_theme(self, self._theme_name)
        # update menu style and content background colors
        # re-apply accent colors where used by created widgets
        theme = THEMES[self._theme_name]
        for widget in self.winfo_children():
            try:
                widget.configure(bg=theme["bg"])
            except Exception:
                pass
        # small user feedback
        ctk.CTkLabel(self, text=f"Theme: {self._theme_name.capitalize()}").place_forget()

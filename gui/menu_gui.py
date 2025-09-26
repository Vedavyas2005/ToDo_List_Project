# this is the main menu panel with buttons to navigate to different GUI operations
# each button triggers a callback function provided by app
# gui/menu_gui.py
import customtkinter as ctk

class MenuPanel(ctk.CTkFrame):
    def __init__(self, master, on_add, on_view, on_update, on_mark_done, on_delete, on_toggle_theme, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.on_add = on_add
        self.on_view = on_view
        self.on_update = on_update
        self.on_mark_done = on_mark_done
        self.on_delete = on_delete
        self.on_toggle_theme = on_toggle_theme
        self._build_ui()

    def _make_button(self, text, command):
        theme = self.winfo_toplevel()._app_theme
        btn = ctk.CTkButton(self, text=text, command=command,
                            fg_color=theme["accent"], hover_color=theme["accent_hover"],
                            corner_radius=8, height=42, font=(None, 12))
        return btn

    def _build_ui(self):
        lbl = ctk.CTkLabel(self, text="To-Do List", font=(None, 20, "bold"))
        lbl.grid(row=0, column=0, pady=(8,12), padx=12)

        self._make_button("Add Task", self.on_add).grid(row=1, column=0, pady=6, padx=12, sticky="ew")
        self._make_button("View Tasks", self.on_view).grid(row=2, column=0, pady=6, padx=12, sticky="ew")
        self._make_button("Update Task", self.on_update).grid(row=3, column=0, pady=6, padx=12, sticky="ew")
        self._make_button("Mark Task Done", self.on_mark_done).grid(row=4, column=0, pady=6, padx=12, sticky="ew")
        self._make_button("Delete Task", self.on_delete).grid(row=5, column=0, pady=6, padx=12, sticky="ew")
        self._make_button("Toggle Theme", self.on_toggle_theme).grid(row=6, column=0, pady=6, padx=12, sticky="ew")
        self._make_button("Exit", lambda: self.master.quit()).grid(row=7, column=0, pady=(18,8), padx=12, sticky="ew")
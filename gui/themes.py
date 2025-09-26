# this is the central theme manager for the GUI: colors, fonts and helper to apply theme
# there are two themes: 'dark' (neon/cherry red) and 'light' (neon blue)
import customtkinter as ctk

THEMES = {
    "dark": {
        "appearance": "Dark",
        "bg": "#0F0F10",
        "fg": "#FFFFFF",
        "accent": "#FF1744",   # cherry / neon red
        "accent_hover": "#FF4568"
    },
    "light": {
        "appearance": "Light",
        "bg": "#FFFFFF",
        "fg": "#000000",
        "accent": "#2979FF",   # neon/sky blue
        "accent_hover": "#59A6FF"
    }
}

# Default font family; uses system fallback if missing
DEFAULT_FONT_FAMILY = ("Helvetica", "Arial", "Segoe UI", "Sans-Serif")

def apply_theme(root, theme_name: str = "dark"):
    # this applies theme globally. `root` is the main Tk window
    # this function will be called before creating many widgets so defaults apply consistently
    theme = THEMES.get(theme_name, THEMES["dark"])
    ctk.set_appearance_mode(theme["appearance"])  # "Dark" or "Light" option this is. hmmmmmm
    root.configure(bg=theme["bg"])
    # store theme on root for other modules to use
    root._app_theme = theme

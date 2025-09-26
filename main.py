# this is the entry point for the todo list app
from gui.app import ToDoApp

def main():
    app = ToDoApp()
    app.mainloop()

if __name__ == "__main__":
    main()

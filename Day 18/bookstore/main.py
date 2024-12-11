from tkinter import *
from components.app import AppUI

def runApp():
    root = Tk()
    app = AppUI(root)

    # start the app
    root.mainloop()


if __name__ == "__main__":
    runApp()

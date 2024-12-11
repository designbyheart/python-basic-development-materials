import tkinter as tk


class NavLink(tk.Toplevel):
    def __init__(self, text, onClick):
        self.text = text
        self.onClick = onClick

        return tk.Button(self, text=self.text).pack()

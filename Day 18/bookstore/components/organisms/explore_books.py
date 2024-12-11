import tkinter as tk
from tkinter import messagebox

class BookFinderComponent:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, pady=20)
        self.frame.pack(padx=30, pady=30)

        # Title Label
        self.title_label = tk.Label(self.frame, text="The easiest way to find the best book!",
                                    font=("Helvetica", 24, "bold"))
        self.title_label.pack(pady=(10, 10))

        # Description Label
        self.description_label = tk.Label(self.frame,
                                          text="With us, you can shop online & help save your high street at the same time",
                                          font=("Helvetica", 14), wraplength=400, justify="center")
        self.description_label.pack(pady=(0, 20))

        # Explore Book Button
        self.explore_button = tk.Button(self.frame, text="EXPLORE BOOK", font=("Helvetica", 14),
                                        command=self.explore_book)
        self.explore_button.pack(pady=(0, 20))

        # Testimonial Frame
        self.testimonial_frame = tk.Frame(self.frame, borderwidth=1, relief="solid")
        self.testimonial_frame.pack(pady=(20, 20))

        # Testimonial Label (User Info)
        self.user_name_label = tk.Label(self.testimonial_frame, text="Jeremy Zucker", font=("Helvetica", 16, "bold"))
        self.user_name_label.pack(pady=(10, 0))

        # Testimonial Text
        self.testimonial_text_label = tk.Label(self.testimonial_frame,
                                               text="The best book store in the world!\nEasy to use and shipping.",
                                               font=("Helvetica", 12), wraplength=280, justify="left")
        self.testimonial_text_label.pack(pady=(0, 10))

    def explore_book(self):
        messagebox.showinfo("Explore Book", "Navigate to book exploration!")

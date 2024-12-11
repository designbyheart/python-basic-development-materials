import tkinter as tk
from tkinter import font as tkFont

# Create the Tkinter application window
root = tk.Tk()
root.title("Navigation Menu")
root.geometry("300x500")  # Adjust window size

# Define font styles
heading_font = tkFont.Font(family="Helvetica", size=20, weight="bold")
item_font = tkFont.Font(family="Helvetica", size=16)  # Normal item font
active_item_font = tkFont.Font(
    family="Helvetica", size=16, weight="bold"
)  # Active (bold) item font

# Frame to hold all the menu labels
menu_frame = tk.Frame(root, bg="white")
menu_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Add "Fiction & Literature" heading
fiction_label = tk.Label(
    menu_frame,
    text="Fiction &\nLiterature",
    font=heading_font,
    fg="black",
    bg="white",
    anchor="w",
    justify="left",
)
fiction_label.pack(anchor="w", pady=5)  # Left align

# Add sub-items under "Fiction & Literature"
thriller_label = tk.Label(
    menu_frame, text="Thriller", font=item_font, fg="gray", bg="white", anchor="w"
)
thriller_label.pack(anchor="w", pady=2)

# Add a divider line
divider_label = tk.Label(
    menu_frame, text="|", font=active_item_font, fg="black", bg="white", anchor="w"
)
divider_label.pack(anchor="w", pady=2)

# Add the active sub-item "Romance"
romance_label = tk.Label(
    menu_frame,
    text="Romance",
    font=active_item_font,
    fg="black",
    bg="white",
    anchor="w",
)
romance_label.pack(anchor="w", pady=2)

young_adult_label = tk.Label(
    menu_frame, text="Young Adult", font=item_font, fg="gray", bg="white", anchor="w"
)
young_adult_label.pack(anchor="w", pady=2)

serial_label = tk.Label(
    menu_frame, text="Serial", font=item_font, fg="gray", bg="white", anchor="w"
)
serial_label.pack(anchor="w", pady=2)

# Add "Non Fiction" section
non_fiction_label = tk.Label(
    menu_frame,
    text="Non Fiction",
    font=heading_font,
    fg="black",
    bg="white",
    anchor="w",
)
non_fiction_label.pack(anchor="w", pady=20)

# Add "Comic" section
comic_label = tk.Label(
    menu_frame, text="Comic", font=heading_font, fg="black", bg="white", anchor="w"
)
comic_label.pack(anchor="w", pady=5)

# Add "Children Book" section
children_book_label = tk.Label(
    menu_frame,
    text="Children Book",
    font=heading_font,
    fg="black",
    bg="white",
    anchor="w",
)
children_book_label.pack(anchor="w", pady=5)

# Start the Tkinter main loop (window runs until closed)
root.mainloop()

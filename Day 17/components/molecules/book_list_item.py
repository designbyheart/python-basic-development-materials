import tkinter as tk

# Create the main Tkinter window
window = tk.Tk()
window.title("You're Not As Alone as You Think")

# Set window size
window.geometry("600x800")
window.configure(bg="white")  # Background color as set in UI

# Define custom fonts
heading_font = ("Helvetica", 36, "bold")
subheading_font = ("Helvetica", 28, "normal")
small_font = ("Helvetica", 14)

# Frame for the "book cover"
cover_frame = tk.Frame(window, bg="#3C78A0", width=400, height=575)
cover_frame.pack(pady=30)

# Add the main heading "YOU'RE NOT AS" and "Alone As You Think"
heading_label1 = tk.Label(
    cover_frame, text="YOU'RE NOT AS", bg="#3C78A0", fg="white", font=heading_font
)
heading_label1.pack(pady=(20, 5))

heading_label2 = tk.Label(
    cover_frame, text="ALONE", bg="#3C78A0", fg="white", font=("Helvetica", 70, "bold")
)
heading_label2.pack()

subheading_label = tk.Label(
    cover_frame, text="AS YOU THINK", bg="#3C78A0", fg="white", font=heading_font
)
subheading_label.pack(pady=(5, 10))

# Add subtitle "THE STORIES OF CHOO CHOO"
choo_label = tk.Label(
    cover_frame,
    text="THE STORIES OF CHOO CHOO",
    bg="#3C78A0",
    fg="white",
    font=small_font,
)
choo_label.pack()

# Adding image of the Choo Choo (must be .gif or .png without PIL)
# Use a PNG image which Tkinter can natively read
image_path = "assets/images/choochoo.png"  # Make sure this path is correct and points to a PNG file
choo_image = tk.PhotoImage(file=image_path)  # Tkinter PhotoImage for .png files
choo_label_image = tk.Label(cover_frame, image=choo_image, bg="#3C78A0")
choo_label_image.pack(pady=10)

# Add the author's name "CITRA MARINA"
author_label = tk.Label(
    cover_frame, text="CITRA MARINA", bg="#3C78A0", fg="white", font=subheading_font
)
author_label.pack(side="bottom", pady=10)

# Add bottom text "The Stories of Choo Choo..." under the cover
bottom_label = tk.Label(
    window,
    text="The Stories of Choo Choo: You're Not as...",
    font=("Helvetica", 20, "bold"),
    bg="white",
    fg="black",
)
bottom_label.pack(pady=20)

# Run the application
window.mainloop()

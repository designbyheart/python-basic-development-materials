import tkinter as tk
from tkinter import font as tkFont
from pathlib import Path

# Create the main Tkinter window
root = tk.Tk()
root.title("Custom Fonts Example")
root.geometry("400x300")

# **Custom Font Path**: Add the path to your custom font file (.ttf or .otf)
# In this example, we assume the font is in the same directory as the script
custom_font_path = Path("custom_font.ttf")  # Replace with your actual font file

# Register the custom font in Tkinter
custom_font = tkFont.Font(root, family="CustomFont", size=20, weight="bold")

# If font is not registered automatically when font family is used
root.tk.call("font", "create", "custom_font_family", "-family", custom_font_path)

# Now, 'custom_font_family' is registered and can be used
label = tk.Label(
    root, text="This is Custom Font", font=("custom_font_family", 25), fg="black"
)
label.pack(pady=30)

# Another label using default font
label_default = tk.Label(root, text="Default Font", font=("Arial", 20), fg="gray")
label_default.pack(pady=20)

# Run the application
root.mainloop()

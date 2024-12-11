import tkinter as tk
from tkinter import messagebox, filedialog
# loading Python Imaging Library
from PIL import ImageTk, Image
import os
import shutil

# To get the dialog box to open when required
from tkinter import filedialog


class BookForm:
    def __init__(self, master):
        self.master = master
        self.master.title("Create New Book")

        # Create the gallery folder if it doesn't exist
        self.gallery_folder = "gallery"
        if not os.path.exists(self.gallery_folder):
            os.makedirs(self.gallery_folder)

        # Title Label and Entry
        self.title_label = tk.Label(master, text="Book Title:")
        self.title_label.pack(pady=(10, 5))
        self.title_entry = tk.Entry(master, width=50)
        self.title_entry.pack(pady=(0, 10))

        # Published Year Label and Entry
        self.year_label = tk.Label(master, text="Published Year:")
        self.year_label.pack(pady=(10, 5))
        self.year_entry = tk.Entry(master, width=50)
        self.year_entry.pack(pady=(0, 10))

        # Author Label and Entry
        self.author_label = tk.Label(master, text="Author:")
        self.author_label.pack(pady=(10, 5))
        self.author_entry = tk.Entry(master, width=50)
        self.author_entry.pack(pady=(0, 10))

        # Image Picker
        self.image_label = tk.Label(master, text="Image:")
        self.image_label.pack(pady=(10, 5))
        self.image_button = tk.Button(master, text="Select Image", command=self.open_img)
        self.image_button.pack(pady=(0, 10))

        self.image_path = None  # To store the path of the selected image

        # Submit Button
        self.submit_button = tk.Button(master, text="Create Book", command=self.submit_book)
        self.submit_button.pack(pady=(20, 10))

    def openfilename(self):

        # open file dialog box to select image
        # The dialogue box has a title "Open"
        filename = filedialog.askopenfilename(title='"pen')
        return filename


    def open_img(self):
        # Select the Imagename  from a folder
        x = self.openfilename()

        # opens the image
        img = Image.open(x)

        # resize the image and apply a high-quality down sampling filter
        img = img.resize((250, 250), Image.LANCZOS)

        # PhotoImage class is used to add image to widgets, icons etc
        img = ImageTk.PhotoImage(img)

        # create a label
        panel = tk.Label(self.master, image = img)

        # set the image as img
        panel.image = img
        panel.grid(row = 2)

    def select_image(self):
        self.image_path = filedialog.askopenfilename(title="Select an Image",
                                                     filetypes=(
                                                     ("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*")))
        if not self.image_path:
            messagebox.showwarning("No Image Selected", "Please select an image file.")
        else:
            print(f"Selected image path: {self.image_path}")  # Debug print
            messagebox.showinfo("Image Selected", "Image successfully selected!")


    def submit_book(self):
        title = self.title_entry.get().strip()
        year = self.year_entry.get().strip()
        author = self.author_entry.get().strip()

        if not title or not year or not author or not self.image_path:
            messagebox.showwarning("Missing Information", "Please fill in all fields and select an image.")
            return

        try:
            file_name = os.path.basename(self.image_path)
            new_image_path = os.path.join(self.gallery_folder, file_name)

            # Debuging: Check if image path is correct
            print(f"Copying image from {self.image_path} to {new_image_path}")  # Debug print
            shutil.copy(self.image_path, new_image_path)
            messagebox.showinfo("Success", f"Book '{title}' created successfully with image saved!")

            # Clear the entries after submission
            self.title_entry.delete(0, tk.END)
            self.year_entry.delete(0, tk.END)
            self.author_entry.delete(0, tk.END)
            self.image_path = None
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = BookForm(root)
    root.mainloop()

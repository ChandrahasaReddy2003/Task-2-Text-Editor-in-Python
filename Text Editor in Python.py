import tkinter as tk
from tkinter import filedialog

# Function to open a file and display its contents in the text editor
def open_file():
    # Use filedialog to open a file and get the filepath
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filepath:
        # Open the file in read mode and read its contents
        with open(filepath, "r") as file:
            # Delete any existing text in the text editor
            text.delete("1.0", tk.END)
            # Insert the file contents into the text editor
            text.insert(tk.END, file.read())

# Function to save the contents of the text editor to a file
def save_file():
    # Use filedialog to save the file and get the filepath
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filepath:
        # Open the file in write mode and write the text editor contents
        with open(filepath, "w") as file:
            file.write(text.get("1.0", tk.END))

# Function to clear the text in the text editor
def clear_text():
    # Delete all the text in the text editor
    text.delete("1.0", tk.END)

# Create the main window of the text editor
root = tk.Tk()
root.title("Simple Text Editor")

# Create a Text widget for the text editing area
text = tk.Text(root)
text.pack()

# Create a menu bar
menu = tk.Menu(root)
root.config(menu=menu)

# Create a "File" menu with "Open", "Save", and "Exit" options
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create an "Edit" menu with a "Clear" option
edit_menu = tk.Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Clear", command=clear_text)

# Start the main event loop for the GUI
root.mainloop()

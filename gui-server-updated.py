import tkinter as tk
from tkinter import ttk

# Function to update the second ComboBox based on the first ComboBox selection
def update_combo2(event):
    selected_method = combo1.get()
    if selected_method == "Symmetric Encryption":
        combo2['values'] = ("DES", "TDES")
    elif selected_method == "Asymmetric Encryption":
        combo2['values'] = ("RSA", "ECC")
    elif selected_method == "Hashing":
        combo2['values'] = ("SHA-256", "MD5")
    else:
        combo2['values'] = ()

# Function to handle button click
def on_button_click():
    print("Cryptography method:", combo1.get())
    print("Algorithm:", combo2.get())
    print("TextArea content:", textarea.get("1.0", tk.END))

# Create the main window
root = tk.Tk()
root.title("Cyber Security Server")
screen_width = 780
screen_height = 780
root.geometry(f"{screen_width}x{screen_height}")
root.resizable(False, True)

# Create a frame for layout purposes
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create the first ComboBox
combo_label1 = ttk.Label(frame, text="Choose cryptography method:")
combo_label1.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

combo1 = ttk.Combobox(frame)
combo1['values'] = ("Symmetric Encryption", "Asymmetric Encryption", "Hashing")
combo1.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
combo1.bind("<<ComboboxSelected>>", update_combo2)

# Create the second ComboBox
combo_label2 = ttk.Label(frame, text="Choose algorithm:")
combo_label2.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

combo2 = ttk.Combobox(frame)
combo2.grid(row=1, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

# Create a TextArea
text_label = ttk.Label(frame, text="Enter text here:")
text_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

textarea = tk.Text(frame, height=10, width=40)
textarea.grid(row=2, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

# Create a Button
button = ttk.Button(frame, text="Send message", command=on_button_click)
button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Run the main event loop
root.mainloop()

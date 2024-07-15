import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Cyber Security Server")
screen_width = 780
screen_height = 780
root.geometry(f"{screen_width}x{screen_height}")
root.resizable(False, True)

# Create a frame for layout purposes
frame = ttk.Frame(root, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

# Create a TextArea for received messages
received_label = ttk.Label(frame, text="Received messages from server:")
received_label.pack(fill=tk.X, padx=5, pady=5)

received_textarea = tk.Text(frame, height=10, width=40)
received_textarea.pack(fill=tk.X, padx=5, pady=5)

# Run the main event loop
root.mainloop()

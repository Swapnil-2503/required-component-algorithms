import tkinter as tk
from tkinter import ttk, scrolledtext
import subprocess
import threading

commands_executed = []
history_index = -1

def update_status(message):
    status_text.config(state=tk.NORMAL)
    status_text.insert(tk.END, message + "\n")
    status_text.config(state=tk.DISABLED)
    status_text.see(tk.END)

def run_command(command):
    global current_process
    current_process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    while True:
        output = current_process.stdout.readline()
        if output:
            update_status(output.strip())
        elif current_process.poll() is not None:
            break
    
    stderr_output = current_process.stderr.read()
    if stderr_output:
        update_status(stderr_output.strip())

def on_command_enter(event=None):
    global history_index
    command = command_entry.get().strip('$ ').strip()
    if command:
        update_status(f"$ {command}")
        command_entry.delete(0, tk.END)
        command_entry.insert(0, "$ ")
        commands_executed.append(command)
        history_index = len(commands_executed)
        threading.Thread(target=run_command, args=(command,), daemon=True).start()

def on_key_up(event):
    global history_index
    if commands_executed and history_index > 0:
        history_index -= 1
        command_entry.delete(0, tk.END)
        command_entry.insert(0, f"$ {commands_executed[history_index]}")

def on_key_down(event):
    global history_index
    if commands_executed and history_index < len(commands_executed) - 1:
        history_index += 1
        command_entry.delete(0, tk.END)
        command_entry.insert(0, f"$ {commands_executed[history_index]}")
    elif history_index == len(commands_executed) - 1:
        history_index += 1
        command_entry.delete(0, tk.END)
        command_entry.insert(0, "$ ")

root = tk.Tk()
root.title("Cyber Security Server")
screen_width = 780
screen_height = 780
root.geometry(f"{screen_width}x{screen_height}")
root.resizable(False, True)

main_frame = ttk.Frame(root, padding=10)
main_frame.pack(expand=True, fill=tk.BOTH)

command_prompt_label = ttk.Label(main_frame, text="Type commands:")
command_prompt_label.pack()

command_entry = ttk.Entry(main_frame)
command_entry.pack(fill=tk.X, pady=10)
command_entry.insert(0, "$ ")
command_entry.bind('<Return>', on_command_enter)
command_entry.bind('<Up>', on_key_up)
command_entry.bind('<Down>', on_key_down)

status_text = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, state=tk.DISABLED, height=20)
status_text.pack(fill=tk.BOTH)

root.mainloop()

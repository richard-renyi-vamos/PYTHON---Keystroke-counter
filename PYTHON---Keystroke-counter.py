import tkinter as tk
import keyboard

def count_keystrokes(event):
    global keystroke_count
    keystroke_count += 1
    keystroke_label.config(text=f"Keystrokes: {keystroke_count}")

keystroke_count = 0

root = tk.Tk()
root.title("Keystroke Counter")

info_label = tk.Label(root, text="Start typing to count keystrokes.")
info_label.pack()

keystroke_label = tk.Label(root, text="Keystrokes: 0")
keystroke_label.pack()

keyboard.hook(count_keystrokes)

root.mainloop()

import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%I:%M:%S %p')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

def toggle_fullscreen():
    is_fullscreen = window.attributes('-fullscreen')
    window.attributes('-fullscreen', not is_fullscreen)

# Create the main window
window = tk.Tk()
window.title("Digital Clock")
window.geometry('400x300')

# Create a label to display the time
clock_label = tk.Label(window, font=("Arial", 80), bg="black", fg="white")
clock_label.pack(pady=50)

# Button to toggle fullscreen mode
fullscreen_button = tk.Button(window, text="Toggle Fullscreen", command=toggle_fullscreen)
fullscreen_button.pack(pady=10)

# Start updating the time
update_time()

# Run the main window's event loop
window.mainloop()

import pyautogui
import tkinter as tk
import threading
import time

def send_message():
    message = message_entry.get()
    pyautogui.typewrite(message)
    pyautogui.press('enter')

def start_bot():
    interval = int(interval_entry.get())
    while True:
        send_message()
        time.sleep(interval)

def start_thread():
    thread = threading.Thread(target=start_bot)
    thread.start()


window = tk.Tk()
window.title("Python Bot")
window.geometry("300x200")


message_label = tk.Label(window, text="Message:")
message_label.pack()
message_entry = tk.Entry(window)
message_entry.pack()

interval_label = tk.Label(window, text="Interval (seconds):")
interval_label.pack()
interval_entry = tk.Entry(window)
interval_entry.pack()

start_button = tk.Button(window, text="Start", command=start_thread)
start_button.pack()


window.mainloop()

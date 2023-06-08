import pyautogui
import tkinter as tk
import threading
import time
import keyboard

bot_running = False
selected_hotkey = ""
message = ""
interval = 0

def send_message():
    pyautogui.typewrite(message)
    pyautogui.press('enter')

def start_bot():
    global bot_running
    while bot_running:
        send_message()
        time.sleep(interval)

def start_thread():
    global bot_running
    if not bot_running:
        bot_running = True
        thread = threading.Thread(target=start_bot)
        thread.start()

def stop_bot():
    global bot_running
    bot_running = False

def toggle_bot():
    global bot_running
    if bot_running:
        stop_bot()
    else:
        start_thread()

def update_hotkey():
    global selected_hotkey
    hotkey_entry.delete(0, tk.END)
    hotkey_entry.insert(0, "Press any key...")
    hotkey_button.configure(state=tk.DISABLED)
    keyboard.on_press(update_hotkey_listener)

def update_hotkey_listener(event):
    global selected_hotkey
    selected_hotkey = event.name
    hotkey_entry.delete(0, tk.END)
    hotkey_entry.insert(0, selected_hotkey)
    hotkey_button.configure(state=tk.NORMAL)
    keyboard.unhook(update_hotkey_listener)

def update_message(event):
    global message
    message = message_entry.get()

def update_interval(event):
    global interval
    interval = int(interval_entry.get())


window = tk.Tk()
window.title("Python Bot")
window.geometry("300x250")


message_label = tk.Label(window, text="Message:")
message_label.pack()
message_entry = tk.Entry(window)
message_entry.pack()
message_entry.bind('<FocusOut>', update_message)

interval_label = tk.Label(window, text="Interval (seconds):")
interval_label.pack()
interval_entry = tk.Entry(window)
interval_entry.pack()
interval_entry.bind('<FocusOut>', update_interval)

hotkey_label = tk.Label(window, text="Hotkey:")
hotkey_label.pack()
hotkey_entry = tk.Entry(window)
hotkey_entry.pack()

start_button = tk.Button(window, text="Start", command=toggle_bot)
start_button.pack()

hotkey_button = tk.Button(window, text="Select Hotkey", command=update_hotkey)
hotkey_button.pack()


window.mainloop()

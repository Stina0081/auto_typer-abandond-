import tkinter as tk
import time
import keyboard
import threading

class AutoMessageBot:
    def __init__(self, interval):
        self.interval = interval
        self.message = "Default message"
        self.key = None
        self.running = False

    def set_message(self, message):
        self.message = message

    def set_key(self, key):
        self.key = key

    def toggle_running(self):
        self.running = not self.running
        if self.running:
            self.start_auto_message()
        else:
            self.stop_auto_message()

    def start_auto_message(self):
        t = threading.Thread(target=self.auto_message_thread)
        t.start()

    def auto_message_thread(self):
        while self.running:
            time.sleep(self.interval)
            if self.key and keyboard.is_pressed(self.key):
                print(self.message)

    def stop_auto_message(self):
        self.running = False


bot = AutoMessageBot(1)


window = tk.Tk()
window.title("Auto Message Bot")


message_label = tk.Label(window, text="Message:")
message_label.pack()
message_entry = tk.Entry(window)
message_entry.pack()


key_label = tk.Label(window, text="Key:")
key_label.pack()
key_var = tk.StringVar(window)
key_var.set("None")
key_option_menu = tk.OptionMenu(window, key_var, "None", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12")
key_option_menu.pack()


interval_label = tk.Label(window, text="Interval (seconds):")
interval_label.pack()
interval_var = tk.StringVar(window)
interval_var.set("1")
interval_option_menu = tk.OptionMenu(window, interval_var, "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
interval_option_menu.pack()


toggle_button = tk.Button(window, text="Start", command=bot.toggle_running)
toggle_button.pack()


def update_bot_settings():
    bot.set_message(message_entry.get())
    selected_key = key_var.get()
    bot.set_key(selected_key if selected_key != "None" else None)
    bot.interval = int(interval_var.get())


message_entry.bind("<KeyRelease>", lambda event: update_bot_settings())
key_var.trace("w", lambda *args: update_bot_settings())
interval_var.trace("w", lambda *args: update_bot_settings())


window.mainloop()

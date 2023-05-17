from tkinter import *
from datetime import datetime
import winsound

class AlarmClock:
    def __init__(self, master):
        self.master = master
        self.master.title("Alarm Clock")
        self.master.geometry("400x250")
        self.master.resizable(0,0)
        self.alarm_time = StringVar()
        self.alarm_time.set("00:00:00")

        # Create the widgets
        self.time_label = Label(self.master, text="Set Alarm Time", font=("Arial", 16))
        self.time_label.pack(pady=10)
        self.time_entry = Entry(self.master, textvariable=self.alarm_time, font=("Arial", 24))
        self.time_entry.pack(pady=10)
        self.time_entry.focus()
        self.set_button = Button(self.master, text="Set Alarm", command=self.set_alarm)
        self.set_button.pack(pady=10)
        self.status_label = Label(self.master, text="", font=("Arial", 16))
        self.status_label.pack(pady=10)
        self.stop_button = Button(self.master, text="Stop Alarm", command=self.stop_alarm, state=DISABLED)
        self.stop_button.pack(pady=10)

    def set_alarm(self):
        try:
            alarm_time = datetime.strptime(self.alarm_time.get(), "%H:%M:%S").time()
            current_time = datetime.now().time()
            if alarm_time <= current_time:
                self.status_label.config(text="Please enter a valid time in the future")
            else:
                self.status_label.config(text=f"Alarm set for {alarm_time.strftime('%I:%M:%S %p')}")
                self.time_entry.config(state=DISABLED)
                self.set_button.config(state=DISABLED)
                self.stop_button.config(state=NORMAL)
                self.play_alarm(alarm_time)
        except ValueError:
            self.status_label.config(text="Please enter a valid time in the format HH:MM:SS")

    def play_alarm(self, alarm_time):
        while True:
            current_time = datetime.now().time()
            if current_time >= alarm_time:
                winsound.PlaySound("alarm.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
                break

    def stop_alarm(self):
        winsound.PlaySound(None, winsound.SND_ASYNC)
        self.status_label.config(text="")
        self.time_entry.config(state=NORMAL)
        self.set_button.config(state=NORMAL)
        self.stop_button.config(state=DISABLED)

root = Tk()
app = AlarmClock(root)
root.mainloop()

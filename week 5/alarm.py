from tkinter import *
import datetime
import time
import winsound
from threading import *

hours = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']
minutes = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55','56','57','58','59']

def update_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    time_label.config(text=f"Current Time: {current_time}")
    root.after(1000, update_time)  # Update every 1000 milliseconds (1 second)

def alarm():
    set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
    label.config(text=f"Set Alarm: {set_alarm_time}")
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == set_alarm_time:
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break

def Threading():
    t1 = Thread(target=alarm)
    t1.start()

# Create the main window
root = Tk()
root.title("Alarm Clock")
root.geometry("400x400")

time_label = Label(root, text="Current Time: ", font="20", pady=50)
time_label.pack()

label = Label(root, text="Set Alarm:", font='12')
label.pack(pady=10)

# Create a frame for OptionMenus
options_frame = Frame(root)
options_frame.pack(pady=20)

# Hours OptionMenu
hour_label = Label(options_frame, text="Set Time: ", font='12')
hour_label.grid(row=0, column=0)
hour = StringVar(root)
hour.set("00")
hour_option = OptionMenu(options_frame, hour, *hours)
hour_option.grid(row=0, column=1)

minute_label = Label(options_frame)
minute_label.grid(row=0, column=2)
minute = StringVar(root)
minute.set("00")
minute_option = OptionMenu(options_frame, minute, *minutes)
minute_option.grid(row=0, column=3)

# Seconds OptionMenu
second_label = Label(options_frame)
second_label.grid(row=0, column=4)
second = StringVar(root)
second.set("00")
second_option = OptionMenu(options_frame, second, *minutes)
second_option.grid(row=0, column=5)

# Start Button
start_button = Button(root, text="Set Alarm", command=Threading, font='12')
start_button.pack(pady=20)

update_time()

root.mainloop()

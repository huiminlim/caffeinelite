from tkinter import Tk, Label, Button
from pynput.keyboard import Controller, Key

keyboard = Controller()  # Create the controller

window = Tk()

window.title("Caffeine Lite")
window.geometry('170x100')

count = 0
current_id = 0
period = 3000  # ms

lbl = Label(window, text="Caffeine Lite")
# lbl1 = Label(window, text="Duration: " + str(period/1000) + " sec")
lbl2 = Label(window, text="Count: 0")
lbl3 = Label(window, text="")

lbl.grid(row=0, sticky="w")
# lbl1.grid(row=1, sticky="w")
lbl2.grid(row=2, sticky="w")
lbl3.grid(row=3, sticky="w")


def task():
    global count
    global current_id
    keyboard.press(Key.f15)
    keyboard.release(Key.f15)
    current_id = window.after(1000, task)
    count += 1
    lbl3.configure(text="F20 button was clicked !!")
    lbl2.configure(text="Count: " + str(count))


def clicked():
    window.after_cancel(current_id)
    lbl3.configure(text="Execution has stopped")
    btn.destroy()


btn = Button(window, text="Click to stop", command=clicked)
btn.grid(row=4, sticky="w")

current_id = window.after(1000, task)
window.mainloop()

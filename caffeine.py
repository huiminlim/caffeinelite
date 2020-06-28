import time
from pynput.keyboard import Controller, Key, Listener, KeyCode

keyboard = Controller()  # Create the controller
delay = 1  # 59secs delay


# def on_press(key):
#     print(key)
#     try:
#         if key.char == 'c':
#             print("here")
#     except AttributeError:
#         pass


# lis = Listener(on_press=on_press)
# lis.start()

while True:
    keyboard.press(Key.f15)
    keyboard.release(Key.f15)
    #print("Press f15")
    time.sleep(delay)  # Sleep for the amount of seconds generated

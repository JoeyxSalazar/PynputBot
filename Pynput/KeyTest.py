from pynput.keyboard import Key, Controller
import keyboard
import time


keys = Controller()
shrek = open("C:\\Users\Joey\Desktop\shrek.txt")


def function():
    counter = 0
    while True:
            if keyboard.is_pressed("9"):
                break
            char = shrek.read(1)
            if char == '':
                break
            keys.press(char)
            time.sleep(.02)
            keys.release(char)
            counter += 1
            if counter == 50:
                counter = 0
                keys.press(Key.enter)
                time.sleep(.02)
                keys.release(Key.enter)


while True:
    if keyboard.is_pressed("`"):
        function()
        break
    
      
from pynput import keyboard
import pygame
import os
import ctypes
import time

def collapse(hide=False):
    """Minimize or hide window."""
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0 if hide else 6)  # SW_HIDE or SW_MINIMIZE

# using pygame to play sound
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
s = pygame.mixer.Sound('sounds/keysound30.wav')
e = pygame.mixer.Sound('sounds/ding3.wav')

# for adding to the startup folder
import getpass
USER_NAME = getpass.getuser()

import sys

application_path = ""

# determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)


def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)

os.system("cls")
if(application_path == ""):
    print("error in adding program to startup\n\n")
else:
    add_to_startup(application_path)

collapse(True)



# using pynput module
def on_press(key):
    if(str(key) == "Key.enter"):
        e.play(loops=0, maxtime=0, fade_ms=0)
    else:
        s.play(loops=0, maxtime=0, fade_ms=0)


# Collect events until released
with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press)
listener.start()



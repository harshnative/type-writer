from sys import path
from pynput import keyboard
import pygame
import os
import ctypes
import sys

# determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)



# function for collapsing the application onces started
def collapse(hide=False):
    """Minimize or hide window."""
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0 if hide else 6)  # SW_HIDE or SW_MINIMIZE


# using pygame to play sound
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)

s = pygame.mixer.Sound( os.path.join(application_path + '\sounds\keysound30.wav'))
e = pygame.mixer.Sound( os.path.join(application_path + '\sounds\ding3.wav'))


# for adding to the startup folder
import getpass
USER_NAME = getpass.getuser()

application_path = application_path + r"\typeWriter.exe"

apPathList = application_path.split("\\")

pathToBat = ""
for i in apPathList:
    pathToBat = pathToBat + '"' + i + '"' + "\\"

pathToBat = pathToBat[:-1]


# function to add file to startup
def add_to_startup(file_path=""):
    
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "typeWriterStartup.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)


add_to_startup(pathToBat)

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
import keyboard

import pygame
import os

pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
s = pygame.mixer.Sound('sounds/keysound30.wav')
e = pygame.mixer.Sound('sounds/ding3.wav')

os.system("cls")
print("close the program to stop making sound")
print("\n\nby harsh native ... contact for your project - harshnative@gmail.com")

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
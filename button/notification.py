import subprocess
import time
import pygame

CMD = '''
on run argv
  display notification (item 2 of argv) with title (item 1 of argv)
end run
'''

def notify(title, text):
  subprocess.call(['osascript', '-e', CMD, title, text])

def alert(message, isBreak):
    notify("Pomodoro timer", message)
    pygame.mixer.init()
    if(isBreak):
      pygame.mixer.music.load("break.mp3")
    else:
      pygame.mixer.music.load("study.mp3")
    pygame.mixer.music.play()

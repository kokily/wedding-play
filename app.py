import os.path
import pygame
import time
import random
import keyboard
import datetime as dt
import sys, traceback
import logging
logging.basicConfig(level=logging.ERROR)

## constants
covid1 = "10:50"
covid2 = "11:20"
covid3 = "12:20"
covid4 = "12:50"
covid5 = "13:50"
covid6 = "14:20"
covid7 = "15:20"
covid8 = "15:50"
covid9 = "16:50"
covid10= "17:20"

folder = "data/"
filenames = []
covidname = 'covid/covid19.mp3'
files = os.listdir(folder)

for i in files:
  filenames.append(folder + i)

def playsound(soundfile):
  pygame.init()
  pygame.mixer.init()
  sound = pygame.mixer.Sound(soundfile)
  clock = pygame.time.Clock()

  sound.set_volume(0.05)
  sound.play()

  while pygame.mixer.get_busy():
    current_time = dt.datetime.now().strftime("%H:%M:%S")

    if current_time == covid1 + ":00" or current_time == covid2 + ":00" or \
        current_time == covid3 + ":00" or current_time == covid4 + ":00" or \
        current_time == covid5 + ":00" or current_time == covid6 + ":00" or \
        current_time == covid7 + ":00" or current_time == covid8 + ":00" or \
        current_time == covid9 + ":00" or current_time == covid10 + ":00":
      sound.stop()
    elif keyboard.is_pressed('p'):
      sound.stop()
      print("<강제> 코로나 방송 송출 중... 이후 음악이 다시 재생됩니다. " + current_time)
      playcovid()
    else:
      clock.tick(1000)

def playcovid():
  pygame.init()
  pygame.mixer.init()
  sound = pygame.mixer.Sound(covidname)
  clock = pygame.time.Clock()

  sound.set_volume(1)
  sound.play()

  while pygame.mixer.get_busy():    
    clock.tick(1000)

def stopmusic():
  pygame.mixer.music.stop()

def getmixerargs():
  pygame.mixer.init()
  freq, size, chan = pygame.mixer.get_init()
  return freq, size, chan

def initMixer():
  BUFFER = 3072
  FREQ, SIZE, CHAN = getmixerargs()
  pygame.mixer.init(FREQ, SIZE, CHAN, BUFFER)

def playcaution():
  current_time = dt.datetime.now().strftime("%H:%M:%S")
  print("코로나19 안내 방송 중... ->" + current_time)
  playcovid()
  stopmusic()

try:
  initMixer()

  while True:    
    current_time = dt.datetime.now().strftime("%H:%M:%S")

    if current_time == covid1 + ":01" or current_time == covid2 + ":01" or \
        current_time == covid3 + ":01" or current_time == covid4 + ":01" or \
        current_time == covid5 + ":01" or current_time == covid6 + ":01" or \
        current_time == covid7 + ":01" or current_time == covid8 + ":01" or \
        current_time == covid9 + ":01" or current_time == covid10 + ":01":
      playcaution()
    else:
      target = random.choice(filenames)
      print("♪~♬ 음악 재생 중 → ", target)
      playsound(target)
      stopmusic()
    
    time.sleep(1)
except KeyboardInterrupt:
  stopmusic()
  print("\n Play stopped by user")
except Exception:
  logging.error(traceback.format_exc())
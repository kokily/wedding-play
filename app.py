import os.path
import pygame
import time
import random
import datetime as dt
import sys, traceback
import logging
logging.basicConfig(level=logging.ERROR)

## constants
covid1 = "10:50"
covid2 = "11:20"
covid3 = "12:30"
covid4 = "12:50"
covid5 = "14:00"
covid6 = "14:20"
covid7 = "15:30"
covid8 = "15:50"
covid9 = "17:00"
covid10= "17:20"

folder = "data/"
filenames = []
covidname = 'data/covid/covid19.mp3'
files = os.listdir(folder)

for i in files:
  filenames.append(folder + i)

def playsound(soundfile):
  pygame.init()
  pygame.mixer.init()
  sound = pygame.mixer.Sound(soundfile)
  clock = pygame.time.Clock()

  sound.set_volume(0.2)
  sound.play()

  while pygame.mixer.get_busy():
    current_time = dt.datetime.now().strftime("%H:%M:%S")

    if current_time == covid1 + ":00" or current_time == covid2 + ":00" or \
        current_time == covid3 + ":00" or current_time == covid4 + ":00" or \
        current_time == covid5 + ":00" or current_time == covid6 + ":00" or \
        current_time == covid7 + ":00" or current_time == covid8 + ":00" or \
        current_time == covid9 + ":00" or current_time == covid10 + ":00":
      sound.stop()
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
  print("Covid19 Caution Print.....")
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
      print("♪~♬ playing song → ", target)
      playsound(target)
      stopmusic()
    
    time.sleep(1)
except KeyboardInterrupt:
  stopmusic()
  print("\n Play stopped by user")
except Exception:
  logging.error(traceback.format_exc())
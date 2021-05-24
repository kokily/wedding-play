import os.path
import pygame
import datetime as dt
import random
import keyboard
import time
import traceback
import logging
logging.basicConfig(level=logging.ERROR)

folder = "data/"
filenames = []
covidname = 'covid/covid19.mp3'
files = os.listdir(folder)
remove_store = 'data/.DS_Store'

if os.path.isfile(remove_store):
  os.remove(remove_store)

for i in files:
  filenames.append(folder + i)

def play_bgm(file):
  pygame.init()
  pygame.mixer.init()

  music = pygame.mixer.Sound(file)
  clock = pygame.time.Clock()

  music.set_volume(0.04)
  music.play()

  while pygame.mixer.get_busy():
    current_time = dt.datetime.now().strftime("%H:%M:%S")

    if keyboard.is_pressed('p'):
      music.stop()
      print("<강제> 코로나 방송 송출 중... 이후 음악이 다시 재생됩니다. " + current_time)
      play_covid()
    else:
      clock.tick(1000)

def play_covid():
  pygame.init()
  pygame.mixer.init()
  sound = pygame.mixer.Sound(covidname)
  clock = pygame.time.Clock()

  sound.set_volume(1)
  sound.play()

  while pygame.mixer.get_busy():
    clock.tick(1000)

def stop_bgm():
  pygame.mixer.music.stop()

def get_mixer_args():
  pygame.mixer.init()
  freq, size, chan = pygame.mixer.get_init()
  return freq, size, chan

def initMixer():
  BUFFER = 3072
  FREQ, SIZE, CHAN = get_mixer_args()
  pygame.mixer.init(FREQ, SIZE, CHAN, BUFFER)

try:
  initMixer()

  while True:
    current_time = dt.datetime.now().strftime("%H:%M:%S")

    target = random.choice(filenames)
    print("♪~♬ 음악 재생 중 → " + target + " <" + current_time + ">")
    play_bgm(target)
    stop_bgm()

    time.sleep(1)
except KeyboardInterrupt:
  stop_bgm()
  print("\n Play stopped by user")
except Exception:
  logging.error(traceback.format_exc())
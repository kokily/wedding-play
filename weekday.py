import os.path
import pygame
import datetime as dt
import random
import time
import traceback
import logging
logging.basicConfig(level=logging.ERROR)

folder = "data/"
filenames = []

files = os.listdir(folder)

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
except Exception:
  logging.error(traceback.format_exc())
import os.path
import pygame
import time
import random
import keyboard
import datetime as dt
import traceback
import logging
logging.basicConfig(level=logging.ERROR)

# Constants
covid = ["10:50","11:20","12:20","12:50","13:50","14:20","15:20","15:50","16:50","17:20"]

# Files and Folders
bgm_folder = "data/"
filenames = []
files = os.listdir(bgm_folder)
covidname = 'covid/covid19.mp3'

# Get BGM Files
for i in files:
  filenames.append(bgm_folder + i)

# Mac remover .DS_Store
if os.path.isfile('data/.DS_Store'):
  print('.DS_Store 파일을 삭제합니다.')
  os.remove('data/.DS_Store')

# Get Today day of week
def get_today_day():
  dotw = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
  return dotw[dt.datetime.today().weekday()]

# Pygame BGM Player Config
def getmixerargs():
  pygame.mixer.init()
  freq, size, chan = pygame.mixer.get_init()
  return freq, size, chan

def initMixer():
  BUFFER = 3072
  FREQ, SIZE, CHAN = getmixerargs()
  pygame.mixer.init(FREQ, SIZE, CHAN, BUFFER)

# Control BGM or Covid19 playing
def play_bgm(file):
  pygame.init()
  pygame.mixer.init()
  bgm = pygame.mixer.Sound(file)
  clock = pygame.time.Clock()

  bgm.set_volume(0.04)
  bgm.play()

  while pygame.mixer.get_busy():
    current_time = dt.datetime.now().strftime("%H:%M:%S")
    target_day = get_today_day()

    if target_day == '토요일' or target_day == '일요일':
      if current_time == covid[0] + ":00" or current_time == covid[1] + ":00" or \
          current_time == covid[2] + ":00" or current_time == covid[3] + ":00" or \
          current_time == covid[4] + ":00" or current_time == covid[5] + ":00" or \
          current_time == covid[6] + ":00" or current_time == covid[7] + ":00" or \
          current_time == covid[8] + ":00" or current_time == covid[9] + ":00":
        bgm.stop()
      elif keyboard.is_pressed('p'):
        bgm.stop()
        print("<강제> 코로나 방송 송출 중... 이후 음악이 다시 재생됩니다. " + current_time)
        play_covid()
    elif keyboard.is_pressed('p'):
      bgm.stop()
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

def general_play():
  current_time = dt.datetime.now().strftime("%H:%M:%S")
  target = random.choice(filenames)
  display = target[5:len(target)-1]

  if display == '.DS_Store':
    os.remove('data/.DS_Store')

  if get_today_day() == '토요일' or get_today_day() == '일요일':
    today = '주말'
  else:
    today = '평일'

  print(f"♪~♬ <{today}> 음악 재생 중 → " + display + " <" + current_time + ">")
  play_bgm(target)
  stop_bgm()

def regular_play():
  current_time = dt.datetime.now().strftime("%H:%M:%S")
  print("코로나19 안내 방송 중... ->" + current_time)
  play_covid()
  stop_bgm()

def stop_bgm():
  pygame.mixer.music.stop()

# Main
try:
  initMixer()

  while True:
    current_time = dt.datetime.now().strftime("%H:%M:%S")
    to_day = get_today_day()

    if to_day == '토요일' or to_day == '일요일':
      if current_time == covid[0] + ":01" or current_time == covid[1] + ":01" or \
        current_time == covid[2] + ":01" or current_time == covid[3] + ":01" or \
        current_time == covid[4] + ":01" or current_time == covid[5] + ":01" or \
        current_time == covid[6] + ":01" or current_time == covid[7] + ":01" or \
        current_time == covid[8] + ":01" or current_time == covid[9] + ":01":
        regular_play()
      else:
        general_play()
    else:
      general_play()

    time.sleep(1)
except KeyboardInterrupt:
  stop_bgm()
  print("\n 프로그램을 임의 종료하였습니다.")
except Exception:
  logging.error(traceback.format_exc())
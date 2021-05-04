import pygame
import time
import datetime as dt
import sys, traceback
import logging
logging.basicConfig(level=logging.ERROR)

## constants
covid1_hour = 
filenames = [
  'data/001.mp3','data/002.mp3','data/003.mp3','data/004.mp3','data/005.mp3','data/006.mp3','data/007.mp3','data/008.mp3','data/009.mp3','data/010.mp3',
  'data/011.mp3','data/012.mp3','data/013.mp3','data/014.mp3','data/015.mp3','data/016.mp3','data/017.mp3','data/018.mp3','data/019.mp3','data/020.mp3',
  'data/021.mp3','data/022.mp3','data/023.mp3','data/024.mp3','data/025.mp3','data/026.mp3','data/027.mp3','data/028.mp3','data/029.mp3','data/030.mp3',
  'data/031.mp3','data/032.mp3','data/033.mp3','data/034.mp3','data/035.mp3','data/036.mp3','data/037.mp3','data/038.mp3','data/039.mp3','data/040.mp3',
  'data/041.mp3','data/042.mp3','data/043.mp3','data/044.mp3','data/045.mp3','data/046.mp3','data/047.mp3','data/048.mp3','data/049.mp3','data/050.mp3',
  'data/051.mp3','data/052.mp3','data/053.mp3','data/054.mp3','data/055.mp3','data/056.mp3','data/057.mp3','data/058.mp3','data/059.mp3','data/060.mp3',
  'data/061.mp3','data/062.mp3','data/063.mp3','data/064.mp3','data/065.mp3','data/066.mp3','data/067.mp3','data/068.mp3','data/069.mp3','data/070.mp3',
  'data/071.mp3','data/072.mp3','data/073.mp3','data/074.mp3','data/075.mp3','data/076.mp3','data/077.mp3','data/078.mp3','data/079.mp3','data/080.mp3',
  'data/081.mp3','data/082.mp3','data/083.mp3','data/084.mp3','data/085.mp3','data/086.mp3','data/087.mp3','data/088.mp3','data/089.mp3','data/090.mp3',
  'data/091.mp3','data/092.mp3','data/093.mp3','data/094.mp3','data/095.mp3','data/096.mp3'
]
covidname = 'data/covid19.mp3'

## Play Sound - 한 방에 메모리 로드
def playsound(soundfile):
  pygame.init()
  pygame.mixer.init()
  sound = pygame.mixer.Sound(soundfile)
  clock = pygame.time.Clock()

  sound.set_volume(0.3)
  sound.play()

  while pygame.mixer.get_busy():
    current_time = dt.datetime.now()

    if current_time.hour == 14 and current_time.minute == 37 and current_time.second == 0:
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

try:
  initMixer()
  sound_num = 1

  while True:    
    current_time = dt.datetime.now()

    if current_time.hour == 14 and current_time.minute == 37 and current_time.second == 1:
      print("Covid19 Caution Print......")
      playcovid()
      stopmusic()
    else:
      print(sound_num)
      print("Playing...Memory -", filenames[sound_num - 1])
      playsound(filenames[sound_num - 1])
      
      if sound_num == 97:
        sound_num = 1
      else:
        sound_num += 1

      stopmusic()
    
    time.sleep(1)
except KeyboardInterrupt:
  stopmusic()
  print("\n Play stopped by user")
except Exception:
  logging.error(traceback.format_exc())
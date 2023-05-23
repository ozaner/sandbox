## A Python script for shiny hunting the Pokkén Gardevoir in Pokémon Insurgence.

from time import sleep
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import pyautogui

m = PyMouse()
k = PyKeyboard()

def action(key: int | str, delay, time_held=.05):
  print("Key Press:", key)
  k.press_key(key)
  sleep(time_held)
  k.release_key(key)
  sleep(delay)

# Color consts
dialogBoxPixel = (235, 241, 255)
normalGardevoirRed = (255, 104, 121)

# Window consts (MUST ADJUST ON NEW LAYOUT)
dialogBoxPos = (488, 232)
normalGardevoirPos = (78, 180)

def test_pixel(delay = 3):
  sleep(delay)
  pos = m.position()
  print("The cursor is currently at: " + str(pos))
  print("Pixel color: ", pyautogui.pixel(*pos))

def hunt(max_iter = -1):
  print('focus window')
  sleep(2)
  m.click(50, 50)
  sleep(1)

  iter = 0
  while (iter < max_iter or max_iter < 0):
    print('1) reset')
    action(k.function_keys[12], 1.5)

    print('2) main menu')
    action(k.enter_key, 1)
    action(k.enter_key, 1)
    action(k.enter_key, 1.5)
    action(k.enter_key, 1.5)

    print('3) text spam')
    action(k.enter_key, 1.1) #open first text box

    currentDialogBoxPixel = (-1, -1, -1)
    while (currentDialogBoxPixel != dialogBoxPixel):
      action(k.enter_key, .3)
      currentDialogBoxPixel = pyautogui.pixel(*dialogBoxPos)

    print('4) refuse nickname')
    sleep(.2)
    action(k.down_key, .2)
    action(k.enter_key, .2)

    print('5) open party')
    action('x', .2)
    action(k.down_key, .2)
    action(k.enter_key, 1.5)
    action(k.right_key, .2)
    action(k.enter_key, .2)
    action(k.enter_key, 1.5)

    print('6) test shiny')
    #tests non-normality (less error-prone)
    if (pyautogui.pixel(*normalGardevoirPos) != normalGardevoirRed):
      print('SHINY?!')
      break
    print('Normal...')
    iter += 1

hunt()
# test_pixel() # Uncomment to find pixel positions
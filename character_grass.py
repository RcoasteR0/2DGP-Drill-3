from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_rectangle():
   print('Rectangle')
   pass

def run_circle():
   print('Circle')
   pass #내용이 없는 빈 함수

while True:
   run_rectangle()
   run_circle() 

close_canvas()

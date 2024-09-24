from pico2d import *

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def run_rectangle():
   print('Rectangle')
   pass

def run_circle():
   print('Circle')
   pass #내용이 없는 빈 함수

clear_canvas_now()
boy.draw_now(400, 300)
delay(1)

while True:
   run_rectangle()
   run_circle()
   break

close_canvas()

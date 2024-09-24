from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def run_rectangle():
   print('Rectangle')
   pass

def run_circle():
   print('Circle')
   pass #내용이 없는 빈 함수

r, cx, cy = 300, 800 // 2, 600 // 2

for degree in range(0, 360, 3):

    theta = math.radians(degree)
    x = r * math.cos(theta) + cx
    y = r * math.sin(theta) + cy

    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.1)

while True:
   run_rectangle()
   run_circle()
   break

close_canvas()

from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def draw_boy(x, y):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.01)

def run_top():
   print('top')
   for x in range(10, 800, 10):
      draw_boy(x, 550)
   pass

def run_right():
   print('right')
   for y in range(550, 50, -10):
      draw_boy(790, y)
   pass

def run_bottom():
   print('bottom')
   for x in range(800, 0, -10):
      draw_boy(x, 60)   
   pass

def run_left():
   print('left')
   for y in range(60, 560, 10):
      draw_boy(10, y)
   pass

def run_rectangle():
   print('Rectangle')
   run_top()
   run_right()
   run_bottom()
   run_left()
   pass

def run_circle():
   print('Circle')
   r, cx, cy = 300, 800 // 2, 600 // 2
   for degree in range(0, 360, 3):
        theta = math.radians(degree)
        x = r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy

        draw_boy(x, y)
   pass #내용이 없는 빈 함수

def run_right_top():
   print('rt')
   x, xmove = 10, 400 / ((560 - 60) // 10)
   for y in range(60, 550, 10):
      draw_boy(x, y)
      x = x + xmove

def run_right_bottom():
   print('rb')
   x, xmove = 400, 400 / ((550 - 50) // 10)
   for y in range(550, 50, -10):
      draw_boy(x, y)
      x = x + xmove


def run_triangle():
   print('Triangle')
   #run_bottom()
   #run_right_top()
   run_right_bottom()

while True:
   #run_rectangle()
   #run_circle()
   run_triangle()
   break

close_canvas()

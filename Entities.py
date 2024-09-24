from pgzero.actor import Actor
from pgzero.keyboard import keyboard
import random

WIDTH = 800
HEIGHT = 600

class GameObject:
  def __init__(self, image, x, y, speed):
    self.actor = Actor(image)
    self.actor.pos = (x, y)
    self.speed = speed

  def update(self):
    self.actor.y += self.speed
    if self.actor.top > HEIGHT:
      self.actor.y = 0
      self.actor.x = random.randint(0, HEIGHT)

  def draw(self):
    self.actor.draw()

class GoodObject(GameObject):
  def __init__(self, x, y, speed):
    super().__init__('good', x, y, speed)

class BadObject(GameObject):
  def __init__(self, x, y, speed):
    super().__init__('bad', x, y, speed)

class Tonks:
  def __init__(self):
    self.actor = Actor('tonks', (WIDTH//2, HEIGHT-50))
    self.score = 0

  def update(self):
    if keyboard.left:
      self.actor.x -= 5
    if keyboard.right:
      self.actor.x += 5
    if self.actor.x <= -50 or self.actor.x >= WIDTH+50:
      self.actor.x = WIDTH//2

  def on_mouse_move(self, pos, rel, buttons):
      self.actor.x = pos[0]

  def draw(self):
    self.actor.draw()

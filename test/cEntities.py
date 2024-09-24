import random
import pgzero as pg
from pgzero.actor import Actor
from pgzero.keyboard import keyboard

WIDTH = 800
HEIGHT = 600

class Objeto:
  def __init__(self, image, x, y, speed):
    self.Actor = Actor(image)
    self.Actor.pos = (x, y)
    self.speed = speed

  def update(self):
    self.Actor.y += self.speed
    if self.Actor.top > HEIGHT:
      self.Actor.y = 0
      self.Actor.x = random.randint(0, WIDTH)

  def draw(self):
    self.Actor.draw()

class GoodObject(Objeto):
  def __init__(self, x, y, speed):
    super().__init__('good', x, y, speed)

class BadObject(Objeto):
  def __init__(self, x, y, speed):
    super().__init__('bad', x, y, speed)

class Tonks:
  def __init__(self):
    self.Actor = Actor('tonks', (WIDTH // 2, HEIGHT - 50))
    self.score = 0

  def update(self):
    if keyboard.left:
      self.Actor.x -= 5
    if keyboard.right:
      self.Actor.x += 5
    self.Actor.x = max(0, min(WIDTH, self.Actor.x))

  def draw(self):
    self.Actor.draw()

  def check_collision(self, good_objects, bad_objects):
    for good in good_objects:
      if self.Actor.colliderect(good.Actor):
        self.score += 1
        good.Actor.y = -50

    for bad in bad_objects:
      if self.Actor.colliderect(bad.Actor):
        self.score -= 1
        bad.Actor.y = -50
        if self.score <= 0:
          self.score = 0

import random
from pgzero.actor import Actor
from pgzero.keyboard import keyboard
import asyncio

WIDTH = 800
HEIGHT = 600
# Note: there's a combination of camelCase and snake_case in the code.
# Lemme explain why: ChatGPT
# -----------------------
# Okno, when im coding, i like to use camelCase for classes, but PGZERO use snake_case for functions and variables.
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
        self.event_handlers = []

    def update(self):
        if keyboard.left:
            self.Actor.x -= 5
        if keyboard.right:
            self.Actor.x += 5
        self.Actor.x = max(0, min(WIDTH, self.Actor.x))

    def draw(self):
        self.Actor.draw()

# EVENTUAL ARCHITECTURE HERE!
    async def emitCollisionEvent(self, objectType, obj):
        for handler in self.event_handlers:
            handler(objectType, obj)

    async def checkCollision(self, godObjects, badObjects):
        for good in godObjects:
            if self.Actor.colliderect(good.Actor):
                self.emitCollisionEvent('good', good)

        for bad in badObjects:
            if self.Actor.colliderect(bad.Actor):
                self.emitCollisionEvent('bad', bad)

    async def onCollision(self, callback):
        self.event_handlers.append(callback)



from eEntities import Tonks, GoodObject, BadObject, WIDTH
import random

tonks = Tonks()
goodObjects = [GoodObject(random.randint(0, WIDTH), random.randint(-100, 0), random.randint(2, 5)) for _ in range(3)]
BadObject = [BadObject(random.randint(0, WIDTH), random.randint(-100, 0), random.randint(2, 5)) for _ in range(3)]

def onCollisionEvent(obj_type, obj):
  if obj_type == 'good':
    tonks.score += 1
    obj.Actor.y = -50 
  elif obj_type == 'bad':
    tonks.score -= 1
    obj.Actor.y = -50 
    if tonks.score < 0:
      tonks.score = 0

tonks.onCollision(onCollisionEvent)

def update():
  tonks.update()
  for obj in goodObjects + BadObject:
    obj.update()
  tonks.checkCollision(goodObjects, BadObject)

def draw():
  screen.clear()
  tonks.draw()
  for obj in goodObjects + BadObject:
    obj.draw()
  screen.draw.text(f"Score: {tonks.score}", (10, 10), fontsize=40, color="white")








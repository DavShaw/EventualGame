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










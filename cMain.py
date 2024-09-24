from cEntities import Tonks, GoodObject, BadObject, WIDTH, HEIGHT
import random
import random

tonks = Tonks()
good_objects = [GoodObject(random.randint(0, WIDTH), random.randint(-100, 0), random.randint(2, 5)) for _ in range(3)]
bad_objects = [BadObject(random.randint(0, WIDTH), random.randint(-100, 0), random.randint(2, 5)) for _ in range(3)]

def update():
  tonks.update()
  for obj in good_objects + bad_objects:
    obj.update()
  tonks.check_collision(good_objects, bad_objects)

def draw():
  screen.clear()
  tonks.draw()
  for obj in good_objects + bad_objects:
    obj.draw()
  screen.draw.text(f"Score: {tonks.score}", (10, 10), fontsize=40, color="white")

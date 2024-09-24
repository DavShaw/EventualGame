from Entities import Tonks, GoodObject, BadObject
from Broker import Broker
import random

class GameEntities:
  def __init__(self):
    self.tonks = Tonks()
    self.good_objects = [GoodObject(random.randint(0, 800), random.randint(-100, 0), random.randint(2, 5)) for _ in range(3)]
    self.bad_objects = [BadObject(random.randint(0, 800), random.randint(-100, 0), random.randint(2, 5)) for _ in range(3)]
    self.broker = Broker()

    # Subscribe to collision events | Explain this
    self.broker.subscribe('collision', self.on_collision_event)

  def on_collision_event(self, obj_type, obj):
    if obj_type == 'good':
      self.tonks.score += 1
      obj.actor.y = -50
    elif obj_type == 'bad':
      self.tonks.score -= 1
      obj.actor.y = -50
      if self.tonks.score < 0:
        self.tonks.score = 0

  def check_collisions(self):
    for good in self.good_objects:
      if self.tonks.actor.colliderect(good.actor):
        self.broker.emit('collision', 'good', good)

    for bad in self.bad_objects:
      if self.tonks.actor.colliderect(bad.actor):
        self.broker.emit('collision', 'bad', bad)

game_entities = GameEntities()

def update():
  game_entities.tonks.update()
  for obj in game_entities.good_objects + game_entities.bad_objects:
    obj.update()
  game_entities.check_collisions()

def draw():
  screen.clear()
  game_entities.tonks.draw()
  for obj in game_entities.good_objects + game_entities.bad_objects:
    obj.draw()
  screen.draw.text(f"Score: {game_entities.tonks.score}", (10, 10), fontsize=40, color="white")

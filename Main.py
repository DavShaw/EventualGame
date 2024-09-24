from Entities import Tonks, GoodObject, BadObject
from Broker import Broker
import random
from Executer import GameEntities

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

def on_mouse_move(pos, rel, buttons):
  game_entities.tonks.on_mouse_move(pos, rel, buttons)
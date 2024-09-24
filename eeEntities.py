import random
from pgzero.actor import Actor
from pgzero.keyboard import keyboard
import asyncio

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
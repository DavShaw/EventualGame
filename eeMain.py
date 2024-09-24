import random
from pgzero.keyboard import keyboard
from eEntities import Tonks, GoodObject, BadObject, Broker, WIDTH, HEIGHT

# Inicialización de objetos
tonks = Tonks()
broker = Broker()
goodObjects = [GoodObject(random.randint(0, WIDTH), random.randint(-100, 0), random.randint(2, 5)) for _ in range(3)]
badObjects = [BadObject(random.randint(0, WIDTH), random.randint(-100, 0), random.randint(2, 5)) for _ in range(3)]

def onCollisionEvent(obj_type, obj):
    if obj_type == 'good':
        tonks.score += 1
        obj.Actor.y = -50 
    elif obj_type == 'bad':
        tonks.score -= 1
        obj.Actor.y = -50 
        if tonks.score < 0:
            tonks.score = 0

# Registramos el evento de colisión
async def setup():
    await broker.onCollision(onCollisionEvent)

# Ejecutamos el setup para registrar el evento de colisión
asyncio.run(setup())

def update():
    tonks.update()
    for obj in goodObjects + badObjects:
        obj.update()
    asyncio.run(broker.checkCollision(tonks, goodObjects, badObjects))

def draw():
    screen.clear()
    tonks.draw()
    for obj in goodObjects + badObjects:
        obj.draw()
    screen.draw.text(f"Score: {tonks.score}", (10, 10), fontsize=40, color="white")

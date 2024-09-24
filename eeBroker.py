import asyncio

class Broker:
    def __init__(self):
        self.event_handlers = []

    async def emitCollisionEvent(self, objectType, obj):
        for handler in self.event_handlers:
            handler(objectType, obj)

    async def checkCollision(self, tonks, goodObjects, badObjects):
        for good in goodObjects:
            if tonks.Actor.colliderect(good.Actor):
                await self.emitCollisionEvent('good', good)

        for bad in badObjects:
            if tonks.Actor.colliderect(bad.Actor):
                await self.emitCollisionEvent('bad', bad)

    async def onCollision(self, callback):
        self.event_handlers.append(callback)

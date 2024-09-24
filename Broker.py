class Broker:
  def __init__(self):
    self.eventHandler = {}

  def subscribe(self, eventType, handler):
    if eventType not in self.eventHandler:
      self.eventHandler[eventType] = []
    self.eventHandler[eventType].append(handler)

  def emit(self, eventType, *args):
    if eventType in self.eventHandler:
      for handler in self.eventHandler[eventType]:
        handler(*args)

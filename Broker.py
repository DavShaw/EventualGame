class Broker:
  def __init__(self):
    self.event_handlers = {}

  def subscribe(self, event_type, handler):
    if event_type not in self.event_handlers:
      self.event_handlers[event_type] = []
    self.event_handlers[event_type].append(handler)

  def emit(self, event_type, *args):
    if event_type in self.event_handlers:
      for handler in self.event_handlers[event_type]:
        handler(*args)

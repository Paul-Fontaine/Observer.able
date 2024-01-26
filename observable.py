from typing import List
from observer import Observer


class Observable:
    def __init__(self, observers: List[Observer] = None):
        self.observers: List[Observer] = observers

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()

class Observer:
    def update(self, obj):
        raise NotImplemented

class Observable:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observer(self, obj):
        for observer in self._observers:
            observer.update(obj)

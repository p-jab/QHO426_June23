from abc import ABC, abstractmethod

class Tech(ABC):

    @abstractmethod
    def activate(self):
        pass


t = Tech()
t.activate()
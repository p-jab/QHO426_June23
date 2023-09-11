from abc import ABC, abstractmethod

class Tech(ABC):

    @abstractmethod
    def activate(self):
        pass

    @abstractmethod
    def deactivate(self):
        pass
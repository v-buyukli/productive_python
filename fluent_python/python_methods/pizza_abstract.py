from abc import ABC, abstractmethod


class BasePizza(ABC):
    @abstractmethod
    def get_radius(self):
        """Method that should do something."""

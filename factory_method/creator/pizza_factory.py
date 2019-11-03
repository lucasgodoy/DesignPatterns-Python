from abc import abstractmethod
from factory_method.product.pizza import Pizza


class PizzaFactory:

    """Factory method"""
    @abstractmethod
    def create_pizza(self) -> Pizza:
        """Creates the concrete object according to required type"""

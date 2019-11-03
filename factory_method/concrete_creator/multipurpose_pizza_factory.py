from factory_method.concrete_product.cheese import CheesePizza
from factory_method.concrete_product.margherita import MargheritaPizza
from factory_method.concrete_product.pepperoni import PepperoniPizza
from factory_method.creator.pizza_factory import PizzaFactory


class MultiPurposePizzaFactory(PizzaFactory):
    """This is also a Factory. It's not necessary each kind of product having its own factory,
    it might be aggregated all in one factory method"""
    def __init__(self, pizza_type):
        self.pizza_type = pizza_type

    def create_pizza(self):
        if self.pizza_type.lower() == "cheese":
            return CheesePizza()
        elif self.pizza_type.lower() == "margherita":
            return MargheritaPizza()
        elif self.pizza_type.lower() == "pepperoni":
            return PepperoniPizza()
        else:
            raise ValueError("Unknown pizza")

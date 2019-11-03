from factory_method.concrete_product.pepperoni import PepperoniPizza
from factory_method.creator.pizza_factory import PizzaFactory


class PepperoniPizzaFactory(PizzaFactory):

    def create_pizza(self):
        return PepperoniPizza()

from factory_method.concrete_product.cheese import CheesePizza
from factory_method.creator.pizza_factory import PizzaFactory


class CheesePizzaFactory(PizzaFactory):

    def create_pizza(self):
        return CheesePizza()

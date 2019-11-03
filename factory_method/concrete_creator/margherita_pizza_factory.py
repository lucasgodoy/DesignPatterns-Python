from factory_method.concrete_product.margherita import MargheritaPizza
from factory_method.creator.pizza_factory import PizzaFactory


class MargheritaPizzaFactory(PizzaFactory):

    def create_pizza(self):
        return MargheritaPizza()

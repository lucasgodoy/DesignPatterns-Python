from factory_method.concrete_creator.cheese_pizza_factory import CheesePizzaFactory
from factory_method.concrete_creator.margherita_pizza_factory import MargheritaPizzaFactory
from factory_method.concrete_creator.multipurpose_pizza_factory import MultiPurposePizzaFactory
from factory_method.concrete_creator.pepperoni_pizza_factory import PepperoniPizzaFactory

if __name__ == "__main__":

    pizza_type = input("Insert type of pizza. Available: cheese, margherita, pepperoni:")
    pizza = "unknown"

    if pizza_type.lower() == "cheese":
        pizza = CheesePizzaFactory().create_pizza()
    elif pizza_type.lower() == "margherita":
        pizza = MargheritaPizzaFactory().create_pizza()
    elif pizza_type.lower() == "pepperoni":
        pizza = PepperoniPizzaFactory().create_pizza()
    else:
        raise ValueError("Unknown pizza")

    print(pizza.get_type())

    """or"""

    print(MultiPurposePizzaFactory(pizza_type).create_pizza().get_type())

from command_pattern.command.prepare_pizza import PreparePizza


class PreparePepperoniPizza(PreparePizza):

    ingredients = ["Pepperoni", "Mozzarella cheese", "Tomato sauce"]

    def __init__(self, pizza_preparer):
        self.pizza_preparer = pizza_preparer

    def execute(self):
        self.pizza_preparer.prepare("Pepperoni", self.ingredients)

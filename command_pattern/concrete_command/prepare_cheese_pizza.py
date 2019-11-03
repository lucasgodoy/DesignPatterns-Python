from command_pattern.command.prepare_pizza import PreparePizza


class PrepareCheesePizza(PreparePizza):

    ingredients = ["Mozzarella cheese", "Parmesan cheese", "Provolone cheese", "Tomato sauce"]

    def __init__(self, pizza_preparer):
        self.pizza_preparer = pizza_preparer

    def execute(self):
        self.pizza_preparer.prepare("Cheese", self.ingredients)

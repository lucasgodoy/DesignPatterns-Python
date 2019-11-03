from factory_method.product.pizza import Pizza


class CheesePizza(Pizza):

    def get_type(self):
        return "Cheese pizza"

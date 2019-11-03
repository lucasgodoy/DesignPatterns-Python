from factory_method.product.pizza import Pizza


class PepperoniPizza(Pizza):

    def get_type(self):
        return "Pepperoni pizza"

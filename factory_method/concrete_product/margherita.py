from factory_method.product.pizza import Pizza


class MargheritaPizza(Pizza):

    def get_type(self):
        return "Margherita pizza"

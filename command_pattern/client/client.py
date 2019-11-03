from command_pattern.concrete_command.prepare_cheese_pizza import PrepareCheesePizza
from command_pattern.receiver.pizza_preparer import PizzaPreparer
from command_pattern.concrete_command.prepare_pepperoni_pizza import PreparePepperoniPizza
from command_pattern.invoker.pizza_operator import PizzaOperator

if __name__ == "__main__":
    pizza_preparer = PizzaPreparer()
    pizza_operator = PizzaOperator()

    prepare_pepperoni = PreparePepperoniPizza(pizza_preparer)
    pizza_operator.execute_operation(prepare_pepperoni)

    prepare_cheese = PrepareCheesePizza(pizza_preparer)
    pizza_operator.execute_operation(prepare_cheese)

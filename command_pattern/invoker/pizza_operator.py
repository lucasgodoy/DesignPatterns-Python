from command_pattern.command.prepare_pizza import PreparePizza


class PizzaOperator:

    def execute_operation(self, command: PreparePizza):
        print("Pizza operator called.")
        command.execute()

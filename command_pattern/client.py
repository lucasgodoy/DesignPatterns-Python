from command_pattern.receiver import Receiver
from command_pattern.concrete_command import ConcreteCommand
from command_pattern.invoker import Invoker


if __name__ == "__main__":
    receiver = Receiver("Any task")
    concrete_command = ConcreteCommand(receiver)
    command_executor = Invoker()
    command_executor.execute_operation(concrete_command)

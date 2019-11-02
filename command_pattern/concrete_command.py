from command_pattern.command import Command


class ConcreteCommand(Command):

    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        print("Concrete command called.")
        self.receiver.do_task()

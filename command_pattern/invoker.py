from command_pattern.command import Command


class Invoker:

    def execute_operation(self, command: Command):
        print("Command executor called.")
        command.execute()

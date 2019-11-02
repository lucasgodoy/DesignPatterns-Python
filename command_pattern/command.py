import abc


class Command:

    @abc.abstractmethod
    def execute(self):
        """Perform command tasks"""

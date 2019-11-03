from abc import abstractmethod


class PreparePizza:

    @abstractmethod
    def execute(self):
        """Perform command tasks to prepare a pizza using ingredients"""

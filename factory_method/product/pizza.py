from abc import abstractmethod


class Pizza:

    @abstractmethod
    def get_type(self) -> str:
        """Returns the type of the pizza"""


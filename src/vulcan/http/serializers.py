from abc import ABC, abstractmethod

class Serializable(ABC):
    """
    Base abstract class (interface) to provide serializable functionality to implementing classes.
    """

    @abstractmethod
    def serialize(self) -> bytes:
        """
        Abstract method that represents a serialization operation to a bytes object. Needs to be implemented in classes
        that extend the base Serializable class.

        :return: The serialized result as a bytes object.
        """
        pass
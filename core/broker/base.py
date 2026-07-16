from abc import ABC, abstractmethod


class Broker(ABC):
    """
    Base interface for all broker integrations.
    """

    @abstractmethod
    def login(self):
        """
        Authenticate with the broker.
        """
        pass

    @abstractmethod
    def logout(self):
        """
        End the broker session.
        """
        pass
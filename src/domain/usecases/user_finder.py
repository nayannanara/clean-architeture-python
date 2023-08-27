from abc import ABC, abstractmethod


class UserFinderInterface(ABC):
    @abstractmethod
    def find(self, first_name: str) -> dict:
        ...

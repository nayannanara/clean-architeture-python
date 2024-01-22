from abc import ABC, abstractmethod


class UserInsertInterface(ABC):
    @abstractmethod
    def insert(self, first_name: str, last_name: str, age: int) -> dict:
        ...

from abc import ABC, abstractmethod


class BaseRule(ABC):

    rule_id: str
    severity: str

    @abstractmethod
    def validate(self, transaction: dict):
        pass
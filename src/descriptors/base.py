from abc import ABC, abstractmethod

from src.logger.setup_logger import logger


class BaseValidator(ABC):
    def __set_name__(self, owner, name):
        self.name = name
        self.private_name = f'_{name}'

    def __get__(self, instance, owner):
        if instance is None:
            logger.warning(f'instance {self} does not exist')
            return self
        return getattr(instance, self.private_name)
    
    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        ...

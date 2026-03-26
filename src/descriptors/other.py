from datetime import datetime

from src.descriptors.base import BaseValidator
from src.core.exceptions import ValidationError
from src.logger.setup_logger import logger


class Const(BaseValidator):
    def __set__(self, instance, value):
        if hasattr(instance, self.private_name):
            raise ValidationError(f'constant {self.name} cannot be changed')
        setattr(instance, self.private_name, value)
    
    def validate(self, value):
        ...
        
class CreatedAt:
    def __get__(self, instance, owner):
        if instance is None:
            logger.warning(f'instance {self} does not exist')
            return self
        if not hasattr(instance, '_created_at'):
            instance._created_at = datetime.now()
        return instance._created_at

    def __set__(self, instance, value):
        raise ValidationError(f'this is a read-only field')

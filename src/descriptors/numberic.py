from src.descriptors.base import BaseValidator
from src.core.exceptions import ValidationError


class IntRange(BaseValidator):
    def __init__(self, min_val=None, max_val=None):
        self.min_val = min_val
        self.max_val = max_val

    def validate(self, value):
        if not isinstance(value, int):
            raise ValidationError(f'{self.name} must be an integer, got {type(value).__name__}')
        if (self.min_val is not None and self.max_val is not None 
            and not (self.min_val <= value <= self.max_val)):
            raise ValidationError(f'{self.name} must be in [{self.min_val}, {self.max_val}]')

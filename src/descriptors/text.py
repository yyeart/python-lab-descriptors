from src.descriptors.base import BaseValidator
from src.core.exceptions import ValidationError


class NotEmptyString(BaseValidator):
    def validate(self, value):
        if not isinstance(value, str):
            raise ValidationError(f'{self.name} must be a string, got {type(value).__name__}')
        if len(value) < 3:
            raise ValidationError(f'{self.name} must have at least 3 characters')
        
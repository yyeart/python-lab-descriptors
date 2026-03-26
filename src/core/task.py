from src.core.exceptions import StateError
from src.descriptors.numberic import IntRange
from src.descriptors.other import Const, CreatedAt
from src.descriptors.text import NotEmptyString
from src.logger.setup_logger import logger


class Task:
    id = Const()
    description = NotEmptyString()
    priority = IntRange(1, 10)
    created_at = CreatedAt()

    ALLOWED_STATUSES = ('Planned', 'In_progress', 'Done', 'Canceled')

    def __init__(self, id: int, description: str, priority: int = 1):
        self.id = id
        self.description = description
        self.priority = priority
        self._status = 'Planned'

    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value: str):
        if value not in self.ALLOWED_STATUSES:
            raise ValueError(f'{value} is an unknown status.'
                             f'Allowed statuses: {self.ALLOWED_STATUSES}')
        if self._status == 'Done':
            logger.error('attempt to interact with finished task')
            raise StateError('task is already done')
        self._status = value

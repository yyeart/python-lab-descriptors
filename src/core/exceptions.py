class TaskError(Exception):
    ...


class ValidationError(TaskError):
    ...

class StateError(TaskError):
    ...
    
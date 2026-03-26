from src.core.exceptions import TaskError
from src.core.task import Task


def main() -> None:
    try:
        task = Task(
            id=123,
            description='a12',
            priority=5
        )
        task.status = 'in process'
        print(task.status)

    except TaskError as e:
        print(f'Raised exception: {e}')

if __name__ == '__main__':
    main()

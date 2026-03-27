from src.core.exceptions import TaskError
from src.core.task import Task
from src.logger.setup_logger import logger

def demo_data_descriptors() -> None:
    """
    Демонстрирует работу data дескрипторов

    :returns: Ничего не возвращает
    :rtype: None
    """
    print('-' * 40)
    print('Demonstration of data descriptors')

    print('Attempt to init with bad priority')
    try: 
        t = Task(id=1, description='Finish lab', priority='first')
    except TaskError as e:
        print(f'Task error: {e}')
        logger.error(f'Task error: {e}')
        
    t = Task(id=1, description='Finish lab', priority=1)

    print('Attempt to change a constant')
    try:
        t.id = 0
    except TaskError as e:
        print(f'Task error: {e}')
        logger.error(f'Task error: {e}')
    
    print('Attempt to set bad description')
    try:
        t.description = 999
    except TaskError as e:
        print(f'Task error: {e}')
        logger.error(f'Task error: {e}')

def demo_non_data_descriptors() -> None:
    """
    Демонстрирует работу non-data дескрипторов

    :returns: Ничего не возвращает
    :rtype: None
    """
    print('-' * 40)
    print('Demonstration of non-data descriptors')

    t = Task(id=2, description='Write documentation', priority=3)

    print(f'Full info:\n{t.full_info}')
    print('Attempt to change full info')
    t.full_info = 'Custom info'
    print(f'Full info now:\n{t.full_info}')
    print(f'Other fields access is unchanged:\n{t.description}')

def demo_properties() -> None:
    """
    Демонстрирует работу вычисляемых свойств property

    :returns: Ничего не возвращает
    :rtype: None
    """
    print('-' * 40)
    print('Demonstration of properties')

    t = Task(id=3, description='Visit lecture', priority=1)
    print('Attempt to get a calculated value')
    print(f'is_executable: {t.is_executable}')
    print('Attemp to change it')
    logger.info('Attempt to change a calculated value')
    try:
        t.is_executable = False
    except AttributeError as e:
        print(e)
        logger.error(e)

    print('Attempt to make forbidden transition')
    try:
        t.status = 'Done'
    except TaskError as e:
        print(f'Task error: {e}')
        logger.error(f'Task error: {e}')
    print('Attempt to make allowed transition')
    t.status = 'In_progress'

    print(f'Check if is_executable changed after status change: {t.is_executable}')

def demo_read_only() -> None:
    """
    Демонстрирует работу полей доступных только для чтения

    :returns: Ничего не возвращает
    :rtype: None
    """
    print('-' * 40)
    print('Demonstration of read only fields')

    t = Task(id=4, description="Take a nap", priority=1)
    print(t.full_info)

    try:
        t.created_at = 'Right now'
    except TaskError as e:
        print(f'Task error: {e}')
        logger.error(f'Task error: {e}')
    

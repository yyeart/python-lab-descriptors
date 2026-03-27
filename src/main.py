from src.demonstration import (demo_data_descriptors,
                               demo_non_data_descriptors,
                               demo_properties,
                               demo_read_only)
from src.logger.setup_logger import logger

def main() -> None:
    """
    Точка входа
    
    :returns: Ничего не возвращает
    :rtype: None
    """
    try:
        logger.info('Demonstration started')
        demo_data_descriptors()
        demo_non_data_descriptors()
        demo_properties()
        demo_read_only()
        logger.info('Demonstration finished')
    except Exception as e:
        print(f'Unexpected error: {e}')
        logger.error(f'Critical error: {e}')

if __name__ == '__main__':
    main()

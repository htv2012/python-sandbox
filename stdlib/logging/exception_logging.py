import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    logger = logging.getLogger('exception_logging')

    logger.info('Exception logging demo')
    try:
        1 / 0
    except:
        logger.exception('Bad boy found')

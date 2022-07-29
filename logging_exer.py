import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s: %(lineno)d]: %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.DEBUG,
                    filename='log.txt')

logger = logging.getLogger('test_logger')

logger.info('An info message')
logger.warning('This will')
logger.debug('Trying something')

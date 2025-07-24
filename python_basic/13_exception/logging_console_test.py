import logging

def say_hello(msg):
    return "Hello " + msg

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')
logging.debug(say_hello('길동'))
logging.debug('End of program')


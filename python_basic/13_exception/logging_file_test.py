import logging

def say_hello(msg):
    return "Hello " + msg

#파일의 내용중 한글 깨짐
# logging.basicConfig(filename='test1.log', level=logging.DEBUG,
#                      format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.debug('Start of program')
# logging.debug(say_hello('길동'))
# logging.debug('End of program')


root_logger= logging.getLogger()
root_logger.setLevel(logging.DEBUG) # or whatever
handler = logging.FileHandler('test.log', 'w', 'utf-8') # or whatever
formatter = logging.Formatter('%(name)s %(message)s') # or whatever
handler.setFormatter(formatter) # Pass handler as a parameter, not assign
root_logger.addHandler(handler)

root_logger.debug('Start of program')
root_logger.debug(say_hello('길동'))
root_logger.debug('End of program')
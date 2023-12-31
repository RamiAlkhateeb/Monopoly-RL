GAME_OUTPUT = False
import logging

def log_file_create(filename):
    logger = logging.getLogger("logging")
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

    file_handler = logging.FileHandler(filename, mode='w')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    """
    Currently logging gameplay only in log file. Uncomment below line to log gameplay on console as well. 
    """
    #logger.addHandler(stream_handler)

    return logger

logger = log_file_create('./logs/seed_2.log')

def game_output(*args, end=" - "):
    if GAME_OUTPUT:
       print(*args, end=end)  
    getattr(logger, 'debug')(end.join(str(a) for a in args))
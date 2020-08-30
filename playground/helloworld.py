import logging
from threading import Thread
import time

def hello():
    logging.info('Hello World!')

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    t = Thread(target=hello)
    t.start()

import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating threads")
    x = threading.Thread(target=thread_function, args=('x',))
    y = threading.Thread(target=thread_function, args=('y',))
    logging.info("Main    : before running threads")
    x.start()
    y.start()
    logging.info("Main    : wait for the threads to finish")
    x.join()
    y.join()
    logging.info("Main    : all done")
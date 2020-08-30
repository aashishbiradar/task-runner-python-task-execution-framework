from logger_manager import logger
from tasks import *
from queue import Queue
from concurrent.futures import ThreadPoolExecutor

class Task:
    def __init__(self, id, name, data):
        self.id = id
        self.name = name
        self.data = data
        self.status = 'STARTED'
    
    def run(self):
        try:
            globals()[self.name](self.data)
            self.status = 'SUCCESS'
        except Exception as e:
            logger.exception(e)
            self.status = 'FAILED'

if __name__ == "__main__":
    taskq = Queue()

    # fetch tasks to execute
    for i in range(5):
        data = {'msg':'TASK RUNNER' }
        task = Task(i, 'hello', data)
        taskq.put(task)
    
    # execute tasks
    with ThreadPoolExecutor(max_workers=2) as executor:
        while not taskq.empty():
            task = taskq.get()
            executor.submit(task.run)

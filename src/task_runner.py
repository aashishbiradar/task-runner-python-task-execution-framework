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
    for i in range(20):
        # hello task
        data = {'msg':'TASK RUNNER' }
        task = Task(i, 'hello', data)
        taskq.put(task)

        # random storage task
        data2 = {}
        task2 = Task(i+20, 'store_random', data2)
        taskq.put(task2)

    print(taskq)
    # execute tasks
    with ThreadPoolExecutor(max_workers=8) as executor:
        while not taskq.empty():
            task = taskq.get()
            executor.submit(task.run)

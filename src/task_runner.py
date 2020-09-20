from queue import Queue
from concurrent.futures import ThreadPoolExecutor
from time import sleep

from logger_manager import logger
from task import Task

class TaskRunner():
    def __init__(self):
        self.queue = Queue()

    def submit_tasks(self, tasksList):
        try:
            tasks = list()
            for t in tasksList:
                if not isinstance(t, Task):
                    if 'data' in t: 
                        t = Task(name = t['name'], data= t['data'])
                    else:
                        t = Task(name = t['name'])
                tasks.append(t)
            Task.objects.insert(tasks)
        except Exception as e:
            logger.exception(e)
    
    def fetch_tasks(self):
        return Task.objects(status='NOT_STARTED')

    def populate_queue(self):
        tasks = self.fetch_tasks()
        for task in tasks:
            self.queue.put(task)
    
    def execute_tasks(self):
        with ThreadPoolExecutor(max_workers=4) as executor:
            while not self.queue.empty():
                task = self.queue.get()
                executor.submit(task.run)
    
    def run(self):
        while True:
            self.populate_queue()
            if not self.queue.empty():
                self.execute_tasks()
            else:
                logger.info('No tasks to execute!')
                sleep(2)

if __name__ == "__main__":
    task_runner = TaskRunner()
    task_runner.run()

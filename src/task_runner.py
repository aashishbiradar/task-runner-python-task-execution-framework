from logger_manager import logger
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
from time import sleep
from task import Task

class TaskRunner():
    def __init__(self):
        self.queue = Queue()

    def submit_tasks(self, tasksList):
        try:
            Task.objects.insert(tasksList)
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
                sleep(2)

if __name__ == "__main__":
    task_runner = TaskRunner()
    task_runner.run()

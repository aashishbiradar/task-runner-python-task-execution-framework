from logger_manager import logger
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
from task_manager import TaskManager

# class Task(TaskStore):
#     def __init__(self, **kwargs):
#         TaskStore.__init__(self, **kwargs)
#     def run(self):
#         try:
#             self.status = 'STARTED'
#             self.save()
#             globals()[self.name](self.data)
#             self.status = 'SUCCESS'
#             self.save()
#         except Exception as e:
#             logger.exception(e)
#             self.status = 'FAILED'

if __name__ == "__main__":
    taskq = Queue()

    while True:
        # fetch tasks to execute
        task_manager = TaskManager()
        tasks = task_manager.get_tasks()
        for task in tasks:
            taskq.put(task)

        # execute tasks
        with ThreadPoolExecutor(max_workers=8) as executor:
            while not taskq.empty():
                task = taskq.get()
                executor.submit(task.run)

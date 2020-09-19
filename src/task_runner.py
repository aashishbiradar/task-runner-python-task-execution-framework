from logger_manager import logger
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
from task_manager import TaskManager
from time import sleep

if __name__ == "__main__":
    taskq = Queue()

    while True:
        # fetch tasks to execute
        task_manager = TaskManager()
        tasks = task_manager.get_tasks()
        for task in tasks:
            taskq.put(task)

        # execute tasks
        with ThreadPoolExecutor(max_workers=4) as executor:
            while not taskq.empty():
                task = taskq.get()
                executor.submit(task.run)
        sleep(2)

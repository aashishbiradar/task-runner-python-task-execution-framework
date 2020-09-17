from logger_manager import logger
from models import Tasks

class TaskManager():
    def submit_tasks(self, tasksList):
        try:
            Tasks.objects.insert(tasksList)
        except Exception as e:
            logger.exception(e)

if __name__ == "__main__":

    # submit tasks to execute
    tasks = []
    for i in range(5):
        # random storage task
        tasks.append(Tasks(name='store_random'))
    task_manager = TaskManager()
    task_manager.submit_tasks(tasks) 


from logger_manager import logger
from models import Task

class TaskManager():
    def submit_tasks(self, tasksList):
        try:
            Task.objects.insert(tasksList)
        except Exception as e:
            logger.exception(e)
    
    def get_tasks(self):
        return Task.objects(status='NOT_STARTED')


if __name__ == "__main__":

    # submit tasks to execute
    tasks = []
    for i in range(1000):
        # random storage task
        tasks.append(Task(name='store_random'))
    task_manager = TaskManager()
    task_manager.submit_tasks(tasks) 


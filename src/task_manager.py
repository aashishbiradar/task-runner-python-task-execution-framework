from task import Task
from task_runner import TaskRunner

if __name__ == "__main__":

    # submit tasks to execute
    tasks = []
    for i in range(1000):
        # random storage task
        tasks.append(Task(name='store_random'))
    task_runner = TaskRunner()
    task_runner.submit_tasks(tasks) 


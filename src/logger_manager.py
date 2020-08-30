import logging
logging.basicConfig(
    format='%(asctime)s [%(name)s] [%(levelname)s]  %(message)s', 
    level=logging.INFO, 
    datefmt='%Y-%m-%d %H:%M:%S'
    )
logger = logging.getLogger('TASK RUNNER')
# ch = logging.StreamHandler()
# ch.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s [%(name)s] [%(levelname)s]  %(message)s', '%Y-%m-%d %H:%M:%S')
# ch.setFormatter(formatter)
# logger.addHandler(ch)
fl = logging.FileHandler("logs/task_runner.log")
logger.addHandler(fl)
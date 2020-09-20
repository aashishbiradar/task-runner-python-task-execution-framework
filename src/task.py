from mongoengine import *
import datetime

from logger_manager import logger
from task_definitions import *

connect('task_runner')

class Task(Document):
    name = StringField(required=True, max_length=120)
    data = DictField(default=dict())
    status = StringField(required=True, max_length=120, default='NOT_STARTED')
    createdOn = DateTimeField(default=datetime.datetime.utcnow)

    def run(self):
        try:
            self.update_status('STARTED')
            globals()[self.name](self.data)
            self.update_status('SUCCESS')
        except Exception as e:
            logger.exception(e)
            self.update_status('FAILED')
    
    def update_status(self, status):
        self.status = status
        self.save()
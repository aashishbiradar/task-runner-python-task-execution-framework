from logger_manager import logger
from mongoengine import *
import datetime
from tasks import *

connect('tast_runner')

class Task(Document):
    name = StringField(required=True, max_length=120)
    data = DictField(default={})
    status = StringField(required=True, max_length=120, default='NOT_STARTED')
    createdOn = DateTimeField(default=datetime.datetime.utcnow)

    def run(self):
        try:
            self.status = 'STARTED'
            self.save()
            globals()[self.name](self.data)
            self.status = 'SUCCESS'
            self.save()
        except Exception as e:
            logger.exception(e)
            self.status = 'FAILED'

class RandomStore(Document):
    randomInteger = IntField(required=True)
    randomString = StringField(required=True, max_length=200)
    saveTime = DateTimeField(default=datetime.datetime.utcnow)
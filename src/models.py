from mongoengine import *
import datetime

from logger_manager import logger
from task_definitions import *

connect('task_runner')

class RandomStore(Document):
    randomInteger = IntField(required=True)
    randomString = StringField(required=True, max_length=200)
    saveTime = DateTimeField(default=datetime.datetime.utcnow)
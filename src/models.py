from mongoengine import *
import datetime

connect('tastrunner')

class Tasks(Document):
    name = StringField(required=True, max_length=120)
    data = DictField(required=True, default={})
    status = StringField(required=True, max_length=120, default='NOT_STARTED')
    createdOn = DateTimeField(default=datetime.datetime.utcnow)

class RandomStore(Document):
    randomInteger = IntField(required=True)
    randomString = StringField(required=True, max_length=200)
    saveTime = DateTimeField(default=datetime.datetime.utcnow)
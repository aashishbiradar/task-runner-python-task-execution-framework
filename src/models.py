from mongoengine import *
import datetime

connect('tastrunner')

class RandomStore(Document):
    randomInteger = IntField(required=True)
    randomString = StringField(required=True, max_length=200)
    saveTime = DateTimeField(default=datetime.datetime.utcnow)
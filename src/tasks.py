from logger_manager import logger
import time, random, string

from models import RandomStore

def hello(data):
    logger.info('Hello '+ str(data['msg']))
    time.sleep(2)

def store_random(data):
    rand_int = random.randint(0, 1000)
    rand_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=100))
    logger.info('storing random data int-> ' + str(rand_int) + ' str-> ' + rand_str)
    randDoc = RandomStore(randomInteger=rand_int, randomString=rand_str)
    randDoc.save()
    count = RandomStore.objects.count()
    logger.info('Random store count-> ' + str(count))





import time
#Import the required modules
import redis
from flask import Flask

#Initialize the modules
app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

#Function to get redis hit count
def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

#Routing '/'
@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)

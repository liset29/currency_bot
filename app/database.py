import motor.motor_asyncio
import redis

import config as con
client = motor.motor_asyncio.AsyncIOMotorClient(f"mongodb://{con.MONGO_HOST}:{con.MONGO_PORT}/")
db = client['TEST_TASK']
collection_users = db['users']


REDIS_HOST = con.REDIS_HOST
REDIS_PORT = con.REDIS_PORT
REDIS_DB = con.REDIS_DB
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)


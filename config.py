import os
from dotenv import load_dotenv


load_dotenv()

token = os.getenv('token')
BANK_URL = os.getenv('BANK_URL')

REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')
REDIS_DB = os.getenv('REDIS_DB')

MONGO_HOST = os.getenv('MONGO_HOST')
MONGO_PORT = os.getenv('MONGO_PORT')
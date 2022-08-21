import os
from pymongo import MongoClient

MONGODB_CONNECTION_STRING = os.environ.get('MONGODB_CONNECTION_STRING')
MONGODB_USER = os.environ.get('MONGODB_USER')
MONGODB_PASSWORD = os.environ.get('MONGODB_PASSWORD')

class MongoDbClient:

    def __init__(self):
        self.connection_string = MONGODB_CONNECTION_STRING.format(MONGODB_USER, MONGODB_PASSWORD)

    def get_database(self, database_name='hemopet'):
        client = MongoClient(self.connection_string)
        return client[database_name]

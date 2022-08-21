from src.infra.client.MongoDbClient import MongoDbClient


class ClinicaRepository:

    def __init__(self, mongo_db_client: MongoDbClient):
        self.db = mongo_db_client.get_database()
        self.collection = self.db['clinica']

    def get_all(self):
        raw_clinica = self.collection.find({}, {'_id': False})
        return [
            raw_clinica
            for raw_clinica in raw_clinica
        ]

    def get_by_id(self, id: str):
        raw_clinica = self.collection.find_one({"id": id}, {'_id': False})
        return raw_clinica

    def update(self, clinica):
        return self.collection.update_one({"id": clinica.id}, {"$set": clinica.reprJSON()})

    def delete_by_id(self, id: str):
        return self.collection.find_one_and_delete({"id": id})

    def insert_one(self, clinica):
        return self.collection.insert_one(clinica.reprJSON())

# from src.domain.adapter.ArtistAdapter import ArtistAdapter
from src.infra.client.MongoDbClient import MongoDbClient


class AnimalRepository:

    def __init__(self, mongo_db_client: MongoDbClient):
        self.db = mongo_db_client.get_database()
        self.collection = self.db['pet']

    def get_all(self):
        raw_animal = self.collection.find({}, {'_id': False}) 
        return [
            raw_animal
            for raw_animal in raw_animal
        ]

    def get_by_id(self, id: str):
        raw_animal = self.collection.find_one({"id": id}, {'_id': False})
        return raw_animal

    def update(self, animal):
        return self.collection.update_one({"id": animal.id}, { "$set": animal.reprJSON() })

    def delete_by_id(self, id: str):
        return self.collection.find_one_and_delete({"id": id})

    def insert_one(self, animal):
        return self.collection.insert_one(animal.reprJSON())


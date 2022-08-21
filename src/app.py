""" Main app """
from flask import Flask, jsonify, request

from src.domain.adapter.AnimalAdapter import AnimalAdapter
from src.infra.client.MongoDbClient import MongoDbClient
from src.infra.repository.AnimalRepository import AnimalRepository

app = Flask(__name__)

animal_adapter = AnimalAdapter()
animal_repository = AnimalRepository(MongoDbClient())


@app.route('/health')
def get_health():
    """ Returns message to perform a system health check"""
    return "OK"


@app.route('/animal', methods=['POST'])
def create_animal():
    """ Register animal """
    
    animal = animal_adapter.from_json(request.get_json())
    
    animal_repository.insert_one(animal)
    
    return jsonify(animal.reprJSON()), 201

@app.route('/animal/<animal_id>', methods=["DELETE"])
def delete_animal(animal_id):
    """ Delete animal by id """

    response = animal_repository.delete_by_id(animal_id)

    if response:
        return jsonify({"message": f"Animal {animal_id} removed.", "status": 200}), 200
    else:
        return jsonify({"message": f"Animal {animal_id} not found!", "status": 404}), 404

@app.route('/animal/<animal_id>', methods=["PUT"])
def update_animal(animal_id):
    """ Update animal by id """

    animal = animal_adapter.from_json(request.get_json())

    if not animal:
        return jsonify({"message": f"Invalid JSON data!", "status": 400}), 400

    response = animal_repository.update(animal)

    if response.matched_count > 0:
        return jsonify({"message": f"Animal {animal_id} updated.", "status": 200}), 200
    else:
        return jsonify({"message": f"Animal {animal_id} not found!", "status": 404}), 404

@app.route('/animal/<animal_id>', methods=["GET"])
def get_animal(animal_id):
    """ Get animal by id """

    response = animal_repository.get_by_id(animal_id)

    if response:
        return jsonify(response), 200
    else:
        return jsonify({"message": f"Animal {animal_id} not found!", "status": 404}), 404

@app.route('/animais', methods=["GET"])
def get_animal_list():
    """ Get all animal by id """

    response = animal_repository.get_all()

    return jsonify(response), 200


print("Starting Recommendation Service")
print("----------------------------------------------------")

""" Main app """
from flask import Flask, jsonify, request

from src.domain.adapter.AnimalAdapter import AnimalAdapter
from src.domain.adapter.ClinicaAdapter import ClinicaAdapter
from src.infra.client.MongoDbClient import MongoDbClient
from src.infra.repository.AnimalRepository import AnimalRepository
from src.infra.repository.ClinicaRepository import ClinicaRepository

app = Flask(__name__)

animal_adapter = AnimalAdapter()
animal_repository = AnimalRepository(MongoDbClient())

clinica_adapter = ClinicaAdapter()
clinica_repository = ClinicaRepository(MongoDbClient())


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
        return jsonify({"message": f"Animal {animal_id} removido.", "status": 200}), 200
    else:
        return jsonify({"message": f"Animal {animal_id} não encontrado!", "status": 404}), 404

@app.route('/animal/<animal_id>', methods=["PUT"])
def update_animal(animal_id):
    """ Update animal by id """

    animal = animal_adapter.from_json(request.get_json())

    if not animal:
        return jsonify({"message": f"Dados inválidos!", "status": 400}), 400

    response = animal_repository.update(animal)

    if response.matched_count > 0:
        return jsonify({"message": f"Animal {animal_id} atualizado.", "status": 200}), 200
    else:
        return jsonify({"message": f"Animal {animal_id} não encontrado!", "status": 404}), 404

@app.route('/animal/<animal_id>', methods=["GET"])
def get_animal(animal_id):
    """ Get animal by id """

    response = animal_repository.get_by_id(animal_id)

    if response:
        return jsonify(response), 200
    else:
        return jsonify({"message": f"Animal {animal_id} não encontrado!", "status": 404}), 404

@app.route('/animais', methods=["GET"])
def get_animal_list():
    """ Get all animal by id """

    response = animal_repository.get_all()

    return jsonify(response), 200


### CLINICA


@app.route('/clinica', methods=['POST'])
def create_clinica():
    """ Register clinica """
    
    clinica = clinica_adapter.from_json(request.get_json())
    
    clinica_repository.insert_one(clinica)
    
    return jsonify(clinica.reprJSON()), 201

@app.route('/clinica/<clinica_id>', methods=["DELETE"])
def delete_clinica(clinica_id):
    """ Delete clinica by id """

    response = clinica_repository.delete_by_id(clinica_id)

    if response:
        return jsonify({"message": f"Clinica {clinica_id} removida.", "status": 200}), 200
    else:
        return jsonify({"message": f"Clinica {clinica_id} não encontrada!", "status": 404}), 404

@app.route('/clinica/<clinica_id>', methods=["PUT"])
def update_clinica(clinica_id):
    """ Update clinica by id """

    clinica = clinica_adapter.from_json(request.get_json())

    if not clinica:
        return jsonify({"message": f"Dados inválidos!", "status": 400}), 400

    response = clinica_repository.update(clinica)

    if response.matched_count > 0:
        return jsonify({"message": f"clinica {clinica_id} atualizada.", "status": 200}), 200
    else:
        return jsonify({"message": f"clinica {clinica_id} não encontrada!", "status": 404}), 404

@app.route('/clinica/<clinica_id>', methods=["GET"])
def get_clinica(clinica_id):
    """ Get clinica by id """

    response = clinica_repository.get_by_id(clinica_id)

    if response:
        return jsonify(response), 200
    else:
        return jsonify({"message": f"clinica {clinica_id} não encontrada!", "status": 404}), 404

@app.route('/clinicas', methods=["GET"])
def get_clinica_list():
    """ Get all clinicas by id """

    response = clinica_repository.get_all()

    return jsonify(response), 200


print("Starting Recommendation Service")
print("----------------------------------------------------")

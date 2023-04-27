from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to the airplane API!'

class Airplane:
    def __init__(self, id, name, manufacturer, year):
        self.id = id
        self.name = name
        self.manufacturer = manufacturer
        self.year = year

airplanes = [
    Airplane(1, 'Boeing 737', 'Boeing', 1967),
    Airplane(2, 'Airbus A320', 'Airbus', 1987),
    Airplane(3, 'Embraer E175', 'Embraer', 2003),
]

@app.route('/api/airplanes', methods=['GET'])
def get_airplanes():
    return jsonify([airplane.__dict__ for airplane in airplanes])

@app.route('/api/airplanes/<int:airplane_id>', methods=['GET'])
def get_airplane(airplane_id):
    airplane = next((airplane for airplane in airplanes if airplane.id == airplane_id), None)
    if airplane:
        return jsonify(airplane.__dict__)
    else:
        return 'Airplane not found', 404

@app.route('/api/airplanes', methods=['POST'])
def add_airplane():
    data = request.get_json()
    airplane = Airplane(len(airplanes) + 1, data['name'], data['manufacturer'], data['year'])
    airplanes.append(airplane)
    return jsonify(airplane.__dict__)

@app.route('/api/airplanes/<int:airplane_id>', methods=['PUT'])
def update_airplane(airplane_id):
    airplane = next((airplane for airplane in airplanes if airplane.id == airplane_id), None)
    if airplane:
        data = request.get_json()
        airplane.name = data['name']
        airplane.manufacturer = data['manufacturer']
        airplane.year = data['year']
        return jsonify(airplane.__dict__)
    else:
        return 'Airplane not found', 404

@app.route('/api/airplanes/<int:airplane_id>', methods=['DELETE'])
def delete_airplane(airplane_id):
    airplane = next((airplane for airplane in airplanes if airplane.id == airplane_id), None)
    if airplane:
        airplanes.remove(airplane)
        return '', 204
    else:
        return 'Airplane not found', 404

if __name__ == '__main__':
    app.run()

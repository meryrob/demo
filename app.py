from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory stores for simplicity
members = []
classes = []

@app.route('/')
def index():
    return jsonify({"message": "Gym Management API"})

# Member endpoints
@app.route('/members', methods=['GET'])
def get_members():
    return jsonify(members)

@app.route('/members', methods=['POST'])
def add_member():
    data = request.get_json()
    if not data or 'name' not in data:
        abort(400, description='Member name is required')
    member = {
        'id': len(members) + 1,
        'name': data['name']
    }
    members.append(member)
    return jsonify(member), 201

# Class endpoints
@app.route('/classes', methods=['GET'])
def get_classes():
    return jsonify(classes)

@app.route('/classes', methods=['POST'])
def add_class():
    data = request.get_json()
    if not data or 'title' not in data:
        abort(400, description='Class title is required')
    gym_class = {
        'id': len(classes) + 1,
        'title': data['title']
    }
    classes.append(gym_class)
    return jsonify(gym_class), 201

if __name__ == '__main__':
    app.run(debug=True)

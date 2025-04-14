from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data
items = [
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Phone", "price": 500}
]

# Home route
@app.route('/')
def home():
    return "Welcome to the Flask REST API!"

# GET all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# GET a specific item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

# POST: Add a new item
@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.json
    new_item["id"] = len(items) + 1  # Assign a new ID
    items.append(new_item)
    return jsonify(new_item), 201

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

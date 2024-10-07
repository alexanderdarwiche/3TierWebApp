from flask import Flask, jsonify, request
from flask_cors import CORS
from flasgger import Swagger
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains
swagger = Swagger(app)  # Initialize Flasgger

DB_CONFIG = {
    'host': os.getenv('DATABASE_HOST'),
    'user': os.getenv('DATABASE_USER'),
    'port': os.getenv('DATABASE_PORT'),
    'password': os.getenv('DATABASE_PASSWORD'),
    'database': os.getenv('DATABASE_NAME')
}

# Initialize Database
def init_db():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS items (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL
    )''')
    conn.commit()
    conn.close()

# API to get all items
@app.route('/api/items', methods=['GET'])
def get_items():
    """
    Get all items.
    ---
    responses:
      200:
        description: A list of items
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              name:
                type: string
    """
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    items = [{'id': row[0], 'name': row[1]} for row in cursor.fetchall()]
    conn.close()
    return jsonify(items)

# API to add a new item
@app.route('/api/items', methods=['POST'])
def add_item():
    """
    Add a new item.
    ---
    parameters:
      - name: item
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
    responses:
      201:
        description: Item added successfully
    """
    data = request.get_json()
    name = data['name']

    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO items (name) VALUES (%s)", (name,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Item added successfully!'}), 201

# API to update an item by ID
@app.route('/api/items/<int:id>', methods=['PUT'])
def update_item(id):
    """
    Update an item by ID.
    ---
    parameters:
      - name: item
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
    responses:
      200:
        description: Item updated successfully
    """
    data = request.get_json()
    name = data['name']
    
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("UPDATE items SET name = %s WHERE id = %s", (name, id))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Item updated successfully!'}), 200

# API to remove an item
@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def remove_item(item_id):
    """
    Remove an item by ID.
    ---
    responses:
      200:
        description: Item removed successfully or not found
    """
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM items WHERE id = %s", (item_id,))
    conn.commit()
    if cursor.rowcount > 0:
        message = 'Item removed successfully!'
    else:
        message = 'Item not found!'
    conn.close()

    return jsonify({'message': message}), 200

# Test the connection to the database
@app.route('/test', methods=['GET'])
def test_connection():
    """
    Test the database connection.
    ---
    responses:
      200:
        description: Database connection successful
    """
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        if conn.is_connected():
            return jsonify({"message": "Connected to the database!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()

# OpenAPI definition endpoint (This can be removed)
@app.route('/swagger.json', methods=['GET'])
def swagger_spec():
    return jsonify(swagger.get_swagger()), 200

if __name__ == '__main__':
    init_db()  # Create table if not exists
    app.run(debug=True)

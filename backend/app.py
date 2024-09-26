from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

# MySQL Database Configuration (Locally)
# DB_CONFIG = {
#    'host': os.getenv('DATABASE_HOST'),
#    'user': os.getenv('DATABASE_USER'),
#    'password': os.getenv('DATABASE_PASSWORD'),
#    'database': os.getenv('DATABASE_NAME')
#}

DB_CONFIG = {
    'host': 'mysql',  # Use the service name defined in docker-compose.yml
    'user': 'appuser',
    'password': 'apppassword',
    'database': 'app_db'
}

# Initialize Database
def init_db():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# API to get all items
@app.route('/api/items', methods=['GET'])
def get_items():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    items = [{'id': row[0], 'name': row[1]} for row in cursor.fetchall()]
    conn.close()
    return jsonify(items)

# API to add a new item
@app.route('/api/items', methods=['POST'])
def add_item():
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
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        if conn.is_connected():
            return jsonify({"message": "Connected to the database!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    init_db()  # Create table if not exists
    app.run(debug=True)

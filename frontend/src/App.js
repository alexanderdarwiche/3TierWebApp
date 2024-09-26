import React, { useState, useEffect } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css'; // Import Bootstrap CSS

function App() {
  const [items, setItems] = useState([]);
  const [newItemName, setNewItemName] = useState('');

  useEffect(() => {
    fetchItems();
  }, []);

  const fetchItems = async () => {
    try {
      const response = await axios.get('http://localhost:5000/api/items');
      setItems(response.data);
    } catch (error) {
      console.error('Error fetching items:', error);
    }
  };

  const addItem = async () => {
    if (!newItemName) return; // Prevent adding empty items
    try {
      await axios.post('http://localhost:5000/api/items', { name: newItemName });
      setNewItemName('');
      fetchItems();  // Refresh the list after adding
    } catch (error) {
      console.error('Error adding item:', error);
    }
  };

  const deleteItem = async (id) => {
    try {
      await axios.delete(`http://localhost:5000/api/items/${id}`);
      fetchItems();  // Refresh the list after deletion
    } catch (error) {
      console.error('Error deleting item:', error);
    }
  };

  return (
    <div className="container mt-5">
      <h1 className="text-center">Items</h1>
      <ul className="list-group mt-3">
        {items.map(item => (
          <li key={item.id} className="list-group-item d-flex justify-content-between align-items-center">
            {item.name}
            <button className="btn btn-danger btn-sm" onClick={() => deleteItem(item.id)}>
              Delete
            </button>
          </li>
        ))}
      </ul>
      <div className="input-group mt-4">
        <input
          type="text"
          className="form-control"
          value={newItemName}
          onChange={(e) => setNewItemName(e.target.value)}
          placeholder="Add new item"
        />
        <div className="input-group-append">
          <button className="btn btn-primary" onClick={addItem}>Add Item</button>
        </div>
      </div>
    </div>
  );
}

export default App;

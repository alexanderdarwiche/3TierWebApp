import React, { useState, useEffect } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css'; // Import Bootstrap CSS

function App() {
  const [items, setItems] = useState([]);
  const [newItemName, setNewItemName] = useState('');
  const [editingItemId, setEditingItemId] = useState(null); // Track the item being edited
  const [editedItemName, setEditedItemName] = useState(''); // Track the new name for the edited item

  // Use environment variable or fallback to localhost for development
  /* In a Azure environment, set the REACT_APP_BACKEND_URL environment variable to the appropriate URL of your backend.
  For example, if your backend is hosted at https://mybackend.azurecontainerapps.io, set that as the environment variable in your Azure configuration.*/
  const backendUrl = process.env.REACT_APP_BACKEND_URL || 'http://localhost:5000';

  useEffect(() => {
    fetchItems();
  }, []);

  const fetchItems = async () => {
    try {
      const response = await axios.get(`${backendUrl}/api/items`);
      setItems(response.data);
    } catch (error) {
      console.error('Error fetching items:', error);
    }
  };

  const addItem = async () => {
    if (!newItemName) return; // Prevent adding empty items
    try {
      await axios.post(`${backendUrl}/api/items`, { name: newItemName });
      setNewItemName('');
      fetchItems();  // Refresh the list after adding
    } catch (error) {
      console.error('Error adding item:', error);
    }
  };

  const deleteItem = async (id) => {
    try {
      await axios.delete(`${backendUrl}/api/items/${id}`);
      fetchItems();  // Refresh the list after deletion
    } catch (error) {
      console.error('Error deleting item:', error);
    }
  };

  const startEditing = (item) => {
    setEditingItemId(item.id); // Set the current item to be edited
    setEditedItemName(item.name); // Set the current item name in the input field
  };

  const cancelEditing = () => {
    setEditingItemId(null); // Exit editing mode
    setEditedItemName(''); // Clear edited item name
  };

  const updateItem = async (id) => {
    if (!editedItemName) return; // Prevent updating with an empty name
    try {
      await axios.put(`${backendUrl}/api/items/${id}`, { name: editedItemName });
      fetchItems();  // Refresh the list after updating
      setEditingItemId(null); // Exit editing mode
      setEditedItemName(''); // Clear the input field
    } catch (error) {
      console.error('Error updating item:', error);
    }
  };

  return (
    <div className="container mt-5">
      <h1 className="text-center">Items</h1>
      <ul className="list-group mt-3">
        {items.map(item => (
          <li key={item.id} className="list-group-item d-flex justify-content-between align-items-center">
            {editingItemId === item.id ? (
              <>
                <input
                  type="text"
                  className="form-control"
                  value={editedItemName}
                  onChange={(e) => setEditedItemName(e.target.value)}
                />
                <button className="btn btn-success btn-sm ml-2" onClick={() => updateItem(item.id)}>
                  Save
                </button>
                <button className="btn btn-secondary btn-sm ml-2" onClick={cancelEditing}>
                  Cancel
                </button>
              </>
            ) : (
              <>
                {item.name}
                <div>
                  <button className="btn btn-warning btn-sm mr-2" onClick={() => startEditing(item)}>
                    Edit
                  </button>
                  <button className="btn btn-danger btn-sm" onClick={() => deleteItem(item.id)}>
                    Delete
                  </button>
                </div>
              </>
            )}
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

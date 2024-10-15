// server.js
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 3000;

// Connect to MongoDB (replace 'your_database_url' and 'your_database_name' with your actual values)
mongoose.connect('mongodb://your_database_url/your_database_name', { useNewUrlParser: true, useUnifiedTopology: true });

// Define a schema for your data
const userSchema = new mongoose.Schema({
  name: String,
  email: String,
  message: String
});

// Create a model based on the schema
const User = mongoose.model('User', userSchema);

// Middleware to parse incoming JSON data
app.use(bodyParser.json());

// Serve your HTML file
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

// Handle form submissions
app.post('/submit', async (req, res) => {
  const { name, email, message } = req.body;

  try {
    // Create a new user in the database
    const newUser = new User({ name, email, message });
    await newUser.save();

    res.status(201).json({ success: true, message: 'Data saved successfully' });
  } catch (error) {
    console.error(error);
    res.status(500).json({ success: false, message: 'Internal Server Error' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});

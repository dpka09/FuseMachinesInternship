# Flask CRUD Application

This is a simple Flask application that demonstrates basic CRUD (Create, Read, Update, Delete) operations using SQLAlchemy and Marshmallow. The application interfaces with a PostgreSQL database and provides RESTful API endpoints for managing an `Info` model.

## Features
- **Flask Framework**: Lightweight and easy-to-use Python framework for building web applications.
- **SQLAlchemy**: Handles database interactions.
- **Marshmallow-SQLAlchemy**: Simplifies data serialization and validation.
- **RESTful Endpoints**: Includes endpoints for CRUD operations.

---

## Installation

### Prerequisites
- Python 3.x
- PostgreSQL database

### Steps
1. Clone the repository or download the source code.
2. Install the required Python libraries:
   ```bash
   pip install flask flask-sqlalchemy marshmallow marshmallow-sqlalchemy

### Set up your PostgreSQL database. Update the app.config['SQLALCHEMY_DATABASE_URI'] in the code with your database credentials:

         postgresql://<username>:<password>@<host>:<port>/<database_name>

### Running the Application
1. Navigate to the directory containing the application file.

2. Run the Flask app:
      python <filename>.py

3. Open your browser or API testing tool (like Postman) and go to http://127.0.0.1:3000.

### API Endpoints
**Base URL**

         http://127.0.0.1:3000

### Endpoints
![image](https://github.com/user-attachments/assets/f39dd867-ed11-4bc9-b0b5-18e51239c4ed)


### Example Payloads
***POST Request***

{
    "name": "John Doe",
    "address": "123 Main Street",
    "age": 30,
    "phone": 1234567890
}


***PUT Request***

{
    "name": "Jane Smith",
    "age": 28
}


### Additional Notes ###

- ***The Info model includes the following fields:***

      - id (Integer): Primary key

      - name (String): Name of the individual

      - address (String): Address of the individual

      - age (Integer): Age of the individual

      - phone (Integer): Phone number of the individual

- ***Ensure your database is running and properly configured before starting the application.***

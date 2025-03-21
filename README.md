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
   ```bash
   postgresql://<username>:<password>@<host>:<port>/<database_name>











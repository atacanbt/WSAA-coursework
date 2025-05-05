# Final Project

This folder contains the final project for the **Web Services and Applications** module. The project is developed based on the concepts and technologies learned throughout the course.

## Project Overview

- **Project Title:** Car Management System 
- **Description:** The project is a web-based application that allows users to view and manage a collection of cars. It is built using Python's Flask framework for the backend and MySQL for the database. 


- **The application provides the following functionalities:**
    - **View Cars**: Display a list of cars stored in the database.
    - **Add New Car**: Add a new car to the database.
    - **Update Car Details**: Modify details of an existing car.
    - **Delete Car**: Remove a car from the database.  

## Setup and Installation

1. Clone the repository:
```bash
git clone https://github.com/atacanbt/WSAA-coursework.git
cd WSAA-coursework/project
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Update `dbconfig.py` with your own credentials. 

4. Database setup:
```sql
CREATE TABLE cars (
    id INT AUTO_INCREMENT PRIMARY KEY,
    brand VARCHAR(255) NOT NULL,
    model VARCHAR(255) NOT NULL,
    year INT NOT NULL,
    price DECIMAL(10,2) NOT NULL
);
```

5. Start server:
```bash
python3 server.py
```

6. Access the web interface:
`http://localhost:5000`

## Project Structure

project/

├── server.py            # Flask application

├── carDAO.py            # Database operations

├── carviewer.html       # Web interface

├── dbconfig.py          # Database configuration

└── requirements.txt     # Dependencies

### Troubleshooting

- Common Issues:
    - Database connection errors: Verify credentials in `dbconfig.py`
    - Missing tables: Ensure you've run the SQL schema
    - CORS errors: Check Flask-CORS configuration
    - Authentication issues: Use mysql_native_password plugin 
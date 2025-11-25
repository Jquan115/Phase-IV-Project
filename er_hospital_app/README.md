# ER Hospital Management System - Phase IV

## Setup Instructions

1. Install Python 3.8 or higher

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Update database credentials in app.py:
```python
def get_db():
    return mysql.connector.connect(
        host='localhost',
        user='your_username',
        password='your_password',
        database='er_hospital_management'
    )
```

4. Ensure your MySQL database is running and has:
   - All tables created from Phase II
   - All stored procedures from Phase III
   - Initial data loaded

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

## Technologies Used

- Backend: Flask (Python web framework)
- Database: MySQL 8.0
- Frontend: HTML, CSS, JavaScript
- Database Connector: mysql-connector-python

## Application Structure

- app.py: Main Flask application with all API endpoints
- templates/index.html: Single-page application interface
- requirements.txt: Python dependencies

## Features

The application provides a web interface for all 15 stored procedures:
- Add Patient
- Record Symptom
- Book Appointment
- Place Order
- Add Staff to Department
- Add Funds
- Assign Nurse to Room
- Assign Room to Patient
- Assign Doctor to Appointment
- Manage Department
- Release Room
- Remove Patient
- Remove Staff from Department
- Complete Appointment
- Complete Orders

And displays all 5 views:
- Room Wise View
- Symptoms Overview View
- Medical Staff View
- Department View
- Outstanding Charges View

## Work Distribution

All team members contributed to:
- Database design and implementation
- Stored procedure development
- Frontend interface design
- Backend API development
- Testing and debugging

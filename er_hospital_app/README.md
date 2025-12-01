# ER Hospital Management System - README

## Setup Instructions

### 1. Install Prerequisites
- Install Python 3.8+
- Install MySQL Server 8.0+

### 2. Setup Database
Open MySQL Workbench and run these files in order:
```sql
source Phase_III_SPViewsTemplate.sql
source Phase_III_SPViewsBasicAutograder.sql
```

### 3. Install Python Dependencies
```bash
pip install flask mysql-connector-python
```

### 4. Configure Database Connection
Open `app.py` and update if needed:
```python
host='127.0.0.1'
user='root'
password=''
database='er_hospital_management'
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open browser and go to:
```
http://127.0.0.1:5000
```

3. Stop server with `Ctrl+C`

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Database**: MySQL 8.0
- **Frontend**: HTML, CSS, JavaScript
- **Database Driver**: mysql-connector-python

The application uses Flask to create API endpoints that call MySQL stored procedures. The frontend uses vanilla JavaScript to send requests to Flask and display results dynamically.

## Work Distribution

We all collectively wrote the code and debugged as a group for all aspects of the assigment. 
from flask import Flask, render_template, request, jsonify
import mysql.connector
from datetime import datetime

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user='er_app_user', # testing shared user
        password='phase4', # testing shared password
        database='er_hospital_management'
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_patient', methods=['POST'])
def add_patient():
    data = request.json
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.callproc('add_patient', [
            data['ssn'], data['firstName'], data['lastName'],
            data['birthdate'], data['address'], data['funds'], data['contact']
        ])
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/record_symptom', methods=['POST'])
def record_symptom():
    data = request.json
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.callproc('record_symptom', [
            data['patientId'], data['numDays'], data['apptDate'],
            data['apptTime'], data['symptomType']
        ])
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    data = request.json
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.callproc('book_appointment', [
            data['patientId'], data['apptDate'], data['apptTime'], data['apptCost']
        ])
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/place_order', methods=['POST'])
def place_order():
    data = request.json
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.callproc('place_order', [
            data['orderNumber'], data['priority'], data['patientId'],
            data['doctorId'], data['cost'], data.get('labType'),
            data.get('drug'), data.get('dosage')
        ])
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/add_staff_to_dept', methods=['POST'])
def add_staff_to_dept():
    data = request.json
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.callproc('add_staff_to_dept', [
            data['deptId'], data['ssn'], data['firstName'], data['lastName'],
            data['birthdate'], data['startDate'], data['address'],
            data['staffId'], data['salary']
        ])
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/add_funds', methods=['POST'])
def add_funds():
    data = request.json
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.callproc('add_funds', [data['ssn'], data['funds']])
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/assign_nurse_to_room', methods=['POST'])
def assign_nurse_to_room():
    data = request.json
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.callproc('assign_nurse_to_room', [data['nurseId'], data['roomNumber']])
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/assign_room_to_patient', methods=['POST'])
def assign_room_to_patient():
    data = request.json
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.callproc('assign_room_to_patient', [
            data['ssn'], data['roomNumber'], data['roomType']
        ])
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/assign_doctor_to_appointment', methods=['POST'])
def assign_doctor_to_appointment():
    data = request.json
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.callproc('assign_doctor_to_appointment', [
            data['patientId'], data['apptDate'], data['apptTime'], data['doctorId']
        ])
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/manage_department', methods=['POST'])
def manage_department():
    data = request.json
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.callproc('manage_department', [data['ssn'], data['deptId']])
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/release_room', methods=['POST'])
def release_room():
    data = request.json
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.callproc('release_room', [data['roomNumber']])
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/remove_patient', methods=['POST'])
def remove_patient():
    data = request.json
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.callproc('remove_patient', [data['ssn']])
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/remove_staff_from_dept', methods=['POST'])
def remove_staff_from_dept():
    data = request.json
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.callproc('remove_staff_from_dept', [data['ssn'], data['deptId']])
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/complete_appointment', methods=['POST'])
def complete_appointment():
    data = request.json
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.callproc('complete_appointment', [
            data['patientId'], data['apptDate'], data['apptTime']
        ])
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/complete_orders', methods=['POST'])
def complete_orders():
    data = request.json
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.callproc('complete_orders', [data['numOrders']])
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/view/<view_name>')
def get_view(view_name):
    try:
        conn = get_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(f'SELECT * FROM {view_name}')
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/get_patients')
def get_patients():
    try:
        conn = get_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT ssn, firstName, lastName FROM patient JOIN person USING(ssn)')
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/get_doctors')
def get_doctors():
    try:
        conn = get_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT ssn, firstName, lastName FROM doctor JOIN person USING(ssn)')
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/get_nurses')
def get_nurses():
    try:
        conn = get_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT ssn, firstName, lastName FROM nurse JOIN person USING(ssn)')
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/get_departments')
def get_departments():
    try:
        conn = get_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT deptId, longName FROM department')
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/get_rooms')
def get_rooms():
    try:
        conn = get_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT roomNumber, roomType FROM room')
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

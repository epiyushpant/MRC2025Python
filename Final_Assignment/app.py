from flask import Flask, render_template, request, jsonify, redirect, url_for
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)

# Database configuration
DATABASE = 'students.db'

def init_db():
    """Initialize the database with students table"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT,
            course TEXT NOT NULL,
            semester INTEGER NOT NULL,
            enrollment_date TEXT NOT NULL,
            status TEXT DEFAULT 'Active'
        )
    ''')
    
    # Insert sample data if table is empty
    cursor.execute('SELECT COUNT(*) FROM students')
    if cursor.fetchone()[0] == 0:
        sample_students = [
            ('Preeti Tamang', 'preetitamang.pkr@gmail.com', '9767293168', 'BICTE', 2, '2023-08-20', 'Active'),
            ('Hari Bahadur', 'hari.bahadur@example.com', '9812345678', 'BICTE', 3, '2023-01-10', 'Active'),
            ('Gita Kumari', 'gita.kumari@example.com', '9867123456', 'BICTE', 1, '2024-01-20', 'Inactive'),
        ]
        
        cursor.executemany('''
            INSERT INTO students (name, email, phone, course, semester, enrollment_date, status)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', sample_students)
    
    conn.commit()
    conn.close()

def get_db_connection():
    """Get database connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    """Home page displaying all students"""
    return render_template('index.html')

@app.route('/api/students', methods=['GET'])
def get_students():
    """API endpoint to get all students"""
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students ORDER BY id DESC').fetchall()
    conn.close()
    
    return jsonify([dict(student) for student in students])

@app.route('/api/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """API endpoint to get a single student"""
    conn = get_db_connection()
    student = conn.execute('SELECT * FROM students WHERE id = ?', (student_id,)).fetchone()
    conn.close()
    
    if student:
        return jsonify(dict(student))
    return jsonify({'error': 'Student not found'}), 404

@app.route('/api/students', methods=['POST'])
def create_student():
    """API endpoint to create a new student"""
    data = request.get_json()
    
    # Validation
    required_fields = ['name', 'email', 'course', 'semester']
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({'error': f'{field} is required'}), 400
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO students (name, email, phone, course, semester, enrollment_date, status)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            data['name'],
            data['email'],
            data.get('phone', ''),
            data['course'],
            int(data['semester']),
            data.get('enrollment_date', datetime.now().strftime('%Y-%m-%d')),
            data.get('status', 'Active')
        ))
        
        student_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return jsonify({'message': 'Student created successfully', 'id': student_id}), 201
        
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Email already exists'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    """API endpoint to update a student"""
    data = request.get_json()
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Check if student exists
        existing = cursor.execute('SELECT * FROM students WHERE id = ?', (student_id,)).fetchone()
        if not existing:
            conn.close()
            return jsonify({'error': 'Student not found'}), 404
        
        cursor.execute('''
            UPDATE students 
            SET name = ?, email = ?, phone = ?, course = ?, semester = ?, status = ?
            WHERE id = ?
        ''', (
            data.get('name', existing['name']),
            data.get('email', existing['email']),
            data.get('phone', existing['phone']),
            data.get('course', existing['course']),
            int(data.get('semester', existing['semester'])),
            data.get('status', existing['status']),
            student_id
        ))
        
        conn.commit()
        conn.close()
        
        return jsonify({'message': 'Student updated successfully'})
        
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Email already exists'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    """API endpoint to delete a student"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
        
        if cursor.rowcount == 0:
            conn.close()
            return jsonify({'error': 'Student not found'}), 404
        
        conn.commit()
        conn.close()
        
        return jsonify({'message': 'Student deleted successfully'})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """API endpoint to get statistics"""
    conn = get_db_connection()
    
    total_students = conn.execute('SELECT COUNT(*) FROM students').fetchone()[0]
    active_students = conn.execute('SELECT COUNT(*) FROM students WHERE status = "Active"').fetchone()[0]
    inactive_students = conn.execute('SELECT COUNT(*) FROM students WHERE status = "Inactive"').fetchone()[0]
    
    semester_stats = conn.execute('''
        SELECT semester, COUNT(*) as count 
        FROM students 
        GROUP BY semester 
        ORDER BY semester
    ''').fetchall()
    
    conn.close()
    
    return jsonify({
        'total_students': total_students,
        'active_students': active_students,
        'inactive_students': inactive_students,
        'semester_distribution': [dict(row) for row in semester_stats]
    })

if __name__ == '__main__':
    # Initialize database
    init_db()
    
    # Run the application
    app.run(debug=True, host='0.0.0.0', port=5000)
# Student Management System - BICTE Programme
## Python Programming Assignment - Mahendra Ratna Campus, Tahachal

A complete Flask web application demonstrating CRUD (Create, Read, Update, Delete) operations using SQLite database. Developed by Preeti Tamang.

## Features

### 🎓 Academic Focus
- Designed specifically for BICTE programme students
- Showcases Mahendra Ratna Campus, Tahachal branding
- Educational demonstration of Flask and SQLite integration

### 💻 Technical Features
- **Full CRUD Operations**: Create, Read, Update, Delete students
- **RESTful API**: JSON-based API endpoints for all operations
- **Real-time Search**: Search students by name, email, or course
- **Status Filtering**: Filter students by Active/Inactive status
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Interactive UI**: Modern, professional interface with animations
- **Data Validation**: Client-side and server-side validation
- **Error Handling**: Comprehensive error handling and user feedback

### 📊 Dashboard Features
- Student statistics (Total, Active, Inactive)
- Semester-wise distribution
- Real-time data updates
- Toast notifications for user actions

### 🛠️ Advanced Features
- Modal forms for add/edit operations
- Confirmation dialogs for deletions
- Loading states and animations
- Auto-populated sample data
- Professional styling with gradients and effects

## Project Structure

```
student-management-system/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── students.db           # SQLite database (auto-created)
├── templates/
│   └── index.html        # Main HTML template
└── static/
    ├── style.css         # CSS styles
    └── script.js         # JavaScript functionality
```

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone or Download Files
Create a new directory and save all the provided files:
- `app.py`
- `requirements.txt`
- Create a `templates` folder and put `index.html` inside it
- Create a `static` folder and put `style.css` and `script.js` inside it

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
python app.py
```

### Step 4: Access the Application
Open your web browser and go to:
```
http://localhost:5000
```

## Database Schema

The application uses SQLite with the following schema:

```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    course TEXT NOT NULL,
    semester INTEGER NOT NULL,
    enrollment_date TEXT NOT NULL,
    status TEXT DEFAULT 'Active'
);
```

## API Endpoints

### Students API
- `GET /api/students` - Get all students
- `GET /api/students/<id>` - Get single student
- `POST /api/students` - Create new student
- `PUT /api/students/<id>` - Update student
- `DELETE /api/students/<id>` - Delete student

### Statistics API
- `GET /api/stats` - Get dashboard statistics

## Sample API Usage

### Create a New Student
```bash
curl -X POST http://localhost:5000/api/students \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Preeti Tamang",
    "email": "preeti.pkr@gmail.com",
    "phone": "987654321",
    "course": "BICTE",
    "semester": 7,
    "status": "Active"
  }'
```

### Get All Students
```bash
curl http://localhost:5000/api/students
```

## Technologies Used

### Backend
- **Flask**: Python web framework
- **SQLite**: Lightweight database
- **Python**: Core programming language

### Frontend
- **HTML5**: Modern semantic markup
- **CSS3**: Advanced styling with flexbox, grid, animations
- **JavaScript (ES6+)**: Modern JavaScript features
- **Font Awesome**: Professional icons

### Design Features
- **Responsive Design**: Mobile-first approach
- **Modern UI**: Professional gradients and animations
- **Accessibility**: Proper contrast and semantic markup
- **User Experience**: Loading states, error handling, confirmations

## Assignment Learning Objectives

This project demonstrates:

1. **Flask Framework**: Routing, templates, request handling
2. **Database Operations**: SQLite integration, CRUD operations
3. **API Development**: RESTful API design and implementation
4. **Frontend Integration**: HTML, CSS, JavaScript coordination
5. **Error Handling**: Server-side and client-side validation
6. **Project Structure**: Professional Flask application organization
7. **User Interface**: Modern web design principles
8. **Data Management**: Database schema design and operations

## Customization

### Adding New Courses
Edit the course dropdown in `templates/index.html`:
```html
<select id="studentCourse" name="course" required>
    <option value="BICTE">BICTE</option>
    <option value="BIT">BIT</option>
    <option value="BCA">BCA</option>
    <option value="Your Course">Your Course</option>
</select>
```

### Modifying Styles
Edit `static/style.css` to customize:
- Colors and gradients
- Layout and spacing
- Animations and transitions
- Responsive breakpoints

### Extending Functionality
Add new features by:
- Adding new routes in `app.py`
- Creating new API endpoints
- Enhancing the database schema
- Adding new UI components

## Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   python app.py
   # If port 5000 is busy, change in app.py:
   app.run(debug=True, host='0.0.0.0', port=5001)
   ```

2. **Database Permissions**
   - Ensure write permissions in the project directory
   - Database file `students.db` will be created automatically

3. **Missing Dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

## Academic Note

This project serves as a comprehensive example for BICTE students at Mahendra Ratna Campus, Tahachal, demonstrating:
- Full-stack web development with Flask
- Database integration and management  
- Modern frontend development practices
- Professional code organization and documentation

Perfect for understanding web development concepts, database operations, and creating professional web applications.

---

**Developed for BICTE Programme | Mahendra Ratna Campus, Tahachal**  
*Python Programming Assignment - Flask CRUD Application*
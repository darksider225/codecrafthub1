Here’s an updated **README.md** that matches your current `app.py` (including the new `/api/courses/stats` endpoint):

```markdown
# CodeCraftHub

## Project Overview
**CodeCraftHub** is a simple personalized learning platform designed to help developers track the courses they want to learn. Built with the Flask framework, this RESTful API allows users to manage their courses with ease. It uses a JSON file for data storage, making it lightweight and easy to set up. This project serves as a practical introduction to building REST APIs using Python.

## Features
- Create a new course with name, description, target completion date, status, and creation timestamp.
- Retrieve all courses or a specific course by ID.
- Update course details based on user input.
- Delete courses that are no longer needed.
- Get statistics about total courses and their distribution by status.
- Error handling for common issues such as missing fields and invalid input.

## Installation Instructions

### Step 1: Prerequisites
- Make sure you have Python 3.x installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).
- You'll also need `pip`, which is included with Python 3.x installations.

### Step 2: Clone the Repository
```bash
git clone https://github.com/yourusername/CodeCraftHub.git
cd CodeCraftHub
```
*(Replace `yourusername` with the actual username of the GitHub repository if applicable.)*

### Step 3: Create a Virtual Environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On macOS or Linux
venv\Scripts\activate     # On Windows
```

### Step 4: Install Dependencies
```bash
pip install Flask
```

## How to Run the Application
Ensure you're in the project directory.  
Run the application by executing:
```bash
python app.py
```
The server will start on `http://127.0.0.1:5000`. You should see output indicating that the Flask development server is running.

---

## API Endpoints Documentation

### 1. Create a New Course
**Endpoint:**  
`POST /api/courses`

**Request Body:**
```json
{
    "name": "Learn Python",
    "description": "A comprehensive Python course",
    "target_date": "2023-12-31",
    "status": "Not Started"
}
```

**Response Example:**
```json
{
    "id": 1,
    "name": "Learn Python",
    "description": "A comprehensive Python course",
    "target_date": "2023-12-31",
    "status": "Not Started",
    "created_at": "2023-10-06T12:34:56.789012"
}
```

---

### 2. Get All Courses
**Endpoint:**  
`GET /api/courses`

**Response Example:**
```json
[
    {
        "id": 1,
        "name": "Learn Python",
        "description": "A comprehensive Python course",
        "target_date": "2023-12-31",
        "status": "Not Started",
        "created_at": "2023-10-06T12:34:56.789012"
    }
]
```

---

### 3. Get a Specific Course
**Endpoint:**  
`GET /api/courses/<id>`

**Response Example:**
```json
{
    "id": 1,
    "name": "Learn Python",
    "description": "A comprehensive Python course",
    "target_date": "2023-12-31",
    "status": "Not Started",
    "created_at": "2023-10-06T12:34:56.789012"
}
```

---

### 4. Update a Course
**Endpoint:**  
`PUT /api/courses/<id>`

**Request Body:**
```json
{
    "name": "Learn Python Advanced",
    "description": "An advanced Python course",
    "target_date": "2024-01-15",
    "status": "In Progress"
}
```

**Response Example:**
```json
{
    "id": 1,
    "name": "Learn Python Advanced",
    "description": "An advanced Python course",
    "target_date": "2024-01-15",
    "status": "In Progress"
}
```

---

### 5. Delete a Course
**Endpoint:**  
`DELETE /api/courses/<id>`

**Response Example:**
```json
{
    "result": true
}
```

---

### 6. Get Course Statistics
**Endpoint:**  
`GET /api/courses/stats`

**Response Example:**
```json
{
    "total_courses": 3,
    "status_counts": {
        "Not Started": 1,
        "In Progress": 1,
        "Completed": 1
    }
}
```

---

## Testing Instructions
You can test the API using **curl** or tools like **Postman**.

### Example curl commands:

**Create a new course:**
```bash
curl -X POST http://127.0.0.1:5000/api/courses \
-H "Content-Type: application/json" \
-d '{"name": "Learn Python", "description": "A comprehensive Python course", "target_date": "2023-12-31", "status": "Not Started"}'
```

**Get all courses:**
```bash
curl -X GET http://127.0.0.1:5000/api/courses
```

**Get course statistics:**
```bash
curl -X GET http://127.0.0.1:5000/api/courses/stats
```

---

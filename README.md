# CodeCraftHub

## Project Overview

**CodeCraftHub** is a personal learning goal tracker that helps users organize and monitor the courses they want to complete. The application combines a **Flask REST API backend** with a **responsive web interface**, allowing users to manage their learning journey without interacting directly with API tools.

Users can add new courses, update their progress, track completion goals, and view all planned learning activities in one place. Course data is stored in a JSON file, making the project lightweight and easy to set up for educational purposes.

---

## Features

### Frontend Features

* Add new courses using an intuitive web form.
* Provide the following course details:

  * Course name
  * Course description
  * Target completion date
  * Learning status
* Clear form inputs with a single click.
* View all saved courses in a dedicated courses section.
* Display the total number of tracked courses.
* Show loading and empty states while retrieving data from the API.

### Backend Features

* Create new courses through REST API endpoints.
* Retrieve all courses or a specific course by ID.
* Update existing course information.
* Delete courses that are no longer relevant.
* Generate statistics about learning progress.
* Store data persistently using a JSON file.
* Validate required fields and handle common errors gracefully.

---

## Technologies Used

### Backend

* Python 3
* Flask

### Frontend

* HTML5
* CSS3
* JavaScript

### Data Storage

* JSON

---

## Installation Instructions

### Step 1: Prerequisites

Ensure you have the following installed:

* Python 3.x
* pip (included with most Python installations)

Download Python from:
[https://www.python.org/downloads/](https://www.python.org/downloads/)

---

### Step 2: Clone the Repository

```bash
git clone https://github.com/yourusername/CodeCraftHub.git
cd CodeCraftHub
```

Replace `yourusername` with the actual GitHub username if applicable.

---

### Step 3: Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

---

### Step 4: Install Dependencies

```bash
pip install Flask Flask-Cors
```

If a `requirements.txt` file exists, install dependencies using:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask server:

```bash
python app.py
```

The application will run locally at:

```text
http://127.0.0.1:5000
```

Open this address in your browser to access the CodeCraftHub interface.

---

## Using the Application

### Adding a Course

Complete the **Add New Course** form by entering:

* Course Name
* Target Date
* Status:

  * Not Started
  * In Progress
  * Completed
* Course Description

Click **Add Course** to save the course.

Use **Clear Form** to reset all fields.

---

### Viewing Courses

The **Courses** section displays all tracked learning goals.

For each course, users can view information such as:

* Course name
* Description
* Target completion date
* Current status

The interface also displays the total number of courses currently being tracked.

---

## API Documentation

### Create a Course

**POST**

```text
/api/courses
```

**Request Body**

```json
{
    "name": "Learn Python",
    "description": "A comprehensive Python course",
    "target_date": "2026-07-31",
    "status": "Not Started"
}
```

---

### Get All Courses

**GET**

```text
/api/courses
```

---

### Get a Course by ID

**GET**

```text
/api/courses/<id>
```

---

### Update a Course

**PUT**

```text
/api/courses/<id>
```

**Request Body**

```json
{
    "name": "Advanced Python",
    "description": "Continue learning advanced concepts",
    "target_date": "2026-08-15",
    "status": "In Progress"
}
```

---

### Delete a Course

**DELETE**

```text
/api/courses/<id>
```

---

### Get Course Statistics

**GET**

```text
/api/courses/stats
```

**Example Response**

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

## Example API Testing

### Create a Course

```bash
curl -X POST http://127.0.0.1:5000/api/courses \
-H "Content-Type: application/json" \
-d '{"name":"Learn Python","description":"A comprehensive Python course","target_date":"2026-07-31","status":"Not Started"}'
```

---

### Retrieve All Courses

```bash
curl -X GET http://127.0.0.1:5000/api/courses
```

---

### Retrieve Statistics

```bash
curl -X GET http://127.0.0.1:5000/api/courses/stats
```

---

## Project Structure

```text
CodeCraftHub/
│
├── app.py               # Flask application
├── courses.json         # JSON data storage
├── templates/
│   └── index.html       # Frontend interface
├── static/
│   ├── styles.css       # Application styling
│   └── script.js        # Frontend logic
├── README.md
└── requirements.txt
```

---

## Future Improvements

* Search and filter courses.
* Sort courses by target date or status.
* Add authentication and user accounts.
* Migrate from JSON storage to a relational database.
* Introduce dashboards and visual progress indicators.

---

## License

This project is intended for educational and learning purposes.

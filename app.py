from flask import Flask, jsonify, request, abort
import json
from datetime import datetime
import os
from flask_cors import CORS


app = Flask(__name__)  # Create a Flask application
CORS(app)  # enables CORS for all routes

# Function to load courses from the JSON file
def load_courses():
    if not os.path.exists('courses.json'):
        return []
    with open('courses.json', 'r') as file:
        return json.load(file)

# Function to save courses to the JSON file
def save_courses(courses):
    with open('courses.json', 'w') as file:
        json.dump(courses, file, indent=4)

# Helper function to validate course status
def is_valid_status(status):
    return status in ["Not Started", "In Progress", "Completed"]

# Endpoint to create a new course
@app.route('/api/courses', methods=['POST'])
def add_course():
    new_course = request.json

    if 'name' not in new_course or 'description' not in new_course or \
       'target_date' not in new_course or 'status' not in new_course:
        abort(400, "Missing required fields: name, description, target_date, status")

    try:
        datetime.strptime(new_course['target_date'], '%Y-%m-%d')
    except ValueError:
        abort(400, "Invalid date format, use YYYY-MM-DD")

    if not is_valid_status(new_course['status']):
        abort(400, "Invalid status value, must be 'Not Started', 'In Progress', or 'Completed'")

    courses = load_courses()
    new_course['id'] = len(courses) + 1
    new_course['created_at'] = datetime.now().isoformat()
    courses.append(new_course)

    save_courses(courses)
    return jsonify(new_course), 201

# Endpoint to get all courses
@app.route('/api/courses', methods=['GET'])
def get_courses():
    courses = load_courses()
    return jsonify(courses)

# Endpoint to get a specific course by ID
@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    courses = load_courses()
    for course in courses:
        if course['id'] == course_id:
            return jsonify(course)
    abort(404, "Course not found")

# Endpoint to update a course by ID
@app.route('/api/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    updated_course = request.json
    courses = load_courses()

    for i, course in enumerate(courses):
        if course['id'] == course_id:
            if 'name' in updated_course:
                course['name'] = updated_course['name']
            if 'description' in updated_course:
                course['description'] = updated_course['description']
            if 'target_date' in updated_course:
                try:
                    datetime.strptime(updated_course['target_date'], '%Y-%m-%d')
                    course['target_date'] = updated_course['target_date']
                except ValueError:
                    abort(400, "Invalid date format, use YYYY-MM-DD")
            if 'status' in updated_course:
                if not is_valid_status(updated_course['status']):
                    abort(400, "Invalid status value")
                course['status'] = updated_course['status']

            save_courses(courses)
            return jsonify(course)
    abort(404, "Course not found")

# Endpoint to delete a course by ID
@app.route('/api/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    courses = load_courses()
    for i, course in enumerate(courses):
        if course['id'] == course_id:
            del courses[i]
            save_courses(courses)
            return jsonify({'result': True})
    abort(404, "Course not found")

# New endpoint to get statistics about courses
@app.route('/api/courses/stats', methods=['GET'])
def get_course_stats():
    courses = load_courses()
    total_courses = len(courses)

    # Count number of courses by status
    status_counts = {
        "Not Started": 0,
        "In Progress": 0,
        "Completed": 0
    }

    for course in courses:
        if course['status'] in status_counts:
            status_counts[course['status']] += 1

    stats = {
        "total_courses": total_courses,
        "status_counts": status_counts
    }
    return jsonify(stats)  # ✅ Properly return JSON response


# Entry point to run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

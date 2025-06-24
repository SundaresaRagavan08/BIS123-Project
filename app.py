from flask import Flask, render_template, request

app = Flask(__name__)

# Sample course data
courses = [
    {'id': 1, 'title': 'Python for Beginners', 'description': 'Learn Python from scratch.'},
    {'id': 2, 'title': 'Web Development', 'description': 'HTML, CSS, and JS for building websites.'},
    {'id': 3, 'title': 'AI Basics', 'description': 'Introduction to Artificial Intelligence.'}
]

@app.route('/')
def home():
    return render_template('index.html', courses=courses)

@app.route('/course/<int:course_id>')
def course_detail(course_id):
    course = next((c for c in courses if c['id'] == course_id), None)
    return render_template('course.html', course=course)

if __name__ == '__main__':
    app.run(debug=True)

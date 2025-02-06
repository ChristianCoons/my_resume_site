from flask import Flask, render_template

app = Flask(__name__)

# Sample project data - you can replace with your own
projects = {
    'project1': {
        'title': 'E-Commerce Platform',
        'image': '/static/images/project1.jpg',
        'description': 'A full-stack e-commerce solution built with React and Node.js'
    },
    'project2': {
        'title': 'Machine Learning Model',
        'image': '/static/images/project2.jpg',
        'description': 'Predictive analytics system using Python and TensorFlow'
    },
    # Add more projects as needed
}

@app.route('/')
def home():
    return render_template('home.html', projects=projects)

@app.route('/project/<project_id>')
def project(project_id):
    if project_id in projects:
        return render_template('project.html', project=projects[project_id])
    return 'Project not found', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
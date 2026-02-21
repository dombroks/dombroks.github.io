#!/usr/bin/env python3
"""
Simple web interface to add projects to Hugo portfolio website
"""
from flask import Flask, render_template, request, redirect, url_for, flash
import os
from datetime import datetime
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this'

PROJECTS_DIR = 'content/projects'
UPLOAD_FOLDER = 'static/img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp', 'svg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """Display all existing projects"""
    projects = []
    if os.path.exists(PROJECTS_DIR):
        for filename in os.listdir(PROJECTS_DIR):
            if filename.endswith('.md'):
                projects.append(filename.replace('.md', '').replace('_', ' ').title())
    return render_template('index.html', projects=projects)

@app.route('/add', methods=['GET', 'POST'])
def add_project():
    """Add a new project"""
    if request.method == 'POST':
        title = request.form.get('title')
        date = request.form.get('date') or datetime.now().strftime('%Y-%m-%d')
        context = request.form.get('context')
        link = request.form.get('link')
        description = request.form.get('description')

        if not title:
            flash('Title is required!', 'error')
            return redirect(url_for('add_project'))

        # Handle image upload
        image_path = request.form.get('image')  # Manual image path input
        if 'image_file' in request.files:
            file = request.files['image_file']
            if file and file.filename and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                # Add timestamp to avoid conflicts
                name, ext = os.path.splitext(filename)
                filename = f"{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}{ext}"

                # Ensure upload folder exists
                os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

                # Save the file
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)

                # Use uploaded image path
                image_path = f"/img/{filename}"
                flash(f'Image uploaded successfully: {filename}', 'success')

        # Create filename from title
        filename = title.lower().replace(' ', '_').replace('-', '_')
        filename = ''.join(c for c in filename if c.isalnum() or c == '_')
        filepath = os.path.join(PROJECTS_DIR, f'{filename}.md')

        # Check if file already exists
        if os.path.exists(filepath):
            flash(f'Project "{title}" already exists!', 'error')
            return redirect(url_for('add_project'))

        # Create markdown content
        content = f"""---
title: "{title}"
date: {date}
image: "{image_path}"
context: "{context}"
link : "{link}"
---
{description}
"""

        # Write file
        os.makedirs(PROJECTS_DIR, exist_ok=True)
        with open(filepath, 'w') as f:
            f.write(content)

        flash(f'Project "{title}" added successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('add_project.html')

@app.route('/view/<project_name>')
def view_project(project_name):
    """View a project's markdown file"""
    filename = project_name.lower().replace(' ', '_')
    filepath = os.path.join(PROJECTS_DIR, f'{filename}.md')

    if not os.path.exists(filepath):
        flash('Project not found!', 'error')
        return redirect(url_for('index'))

    with open(filepath, 'r') as f:
        content = f.read()

    return render_template('view_project.html', project_name=project_name, content=content)

if __name__ == '__main__':
    app.run(debug=True, port=5000)


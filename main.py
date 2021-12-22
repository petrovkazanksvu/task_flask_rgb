import os
from app import app
from compute import define_color
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template, jsonify
from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/test/form/upload_image')
def upload_form():
    return render_template('upload.html')


@app.route('/hello')
def hello_world():
    return 'Hello, Docker!'


@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        flash('Image successfully uploaded and displayed below')
        answer = define_color(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template('upload.html', filename=filename, answer=answer)
    else:
        flash('Allowed image types are -> png, jpg, jpeg, gif')
        return redirect(request.url)


@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


@app.route("/api/determine_dominate_color", methods=["POST"])
def process_image():
    file = request.files['image']
    answer = define_color(file.stream)
    return jsonify({'msg': 'success', 'color': answer})


if __name__ == "__main__":
    app.run(debug=True)
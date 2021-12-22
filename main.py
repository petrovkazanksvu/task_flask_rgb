import os
from app import app
from compute import define_color
from flask import flash, request, redirect, url_for, render_template, jsonify
from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = set(['png'])


def allowed_file(filename):
    """
    Сheck file extension on correсtness
    There are two condition:
    1) filename consist '.'
    2) extension must be 'png'

    :param filename: str
    :return: True or False
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/test/form/upload_image', methods=['GET'])
def upload_form():
    """
    Upload form 'upload.html' for loading file across browser (Method GET)
    :return: rendered html-page from template upload.html
    """
    return render_template('upload.html')


@app.route('/', methods=['POST'])
def upload_image():
    """
    Upload image on server(/static/uploads/) and give answer about domination RGB-color
    Also check file availability and allowed extension
    :return: rendered html-page (with image and dominating color) from template upload.html
    """
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
        flash('Allowed image types are -> png')
        return redirect(request.url)


@app.route('/display/<filename>')
def display_image(filename):
    """
    Display load image on page
    Use in upload.html
    :param filename: filename
    :return: redirect page on image (static/uploads/)
    """
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


@app.route("/api/determine_dominate_color", methods=["POST"])
def receive_image_rest():
    """
    REST-API (POST)
    Also define dominate color across REST-API
    :return: json (example, {'msg': 'success', 'color': 'red'})
    """
    file = request.files['image']
    answer = define_color(file.stream)
    return jsonify({'msg': 'success', 'color': answer})


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, jsonify, send_file
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

DEBUG = True

# Define the path to the upload directory
UPLOAD_FOLDER = 'data/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/api/upload_file', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        print(f'[ERROR] No file in the request.')
        return jsonify({'error': 'No file in the request.'}), 400

    file = request.files['file']

    # if user does not select file, browser may also
    # submit an empty part without filename
    if file.filename == '':
        print(f'No file selected.')
        return jsonify({'error': 'No file selected.'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print(f'File {filename} successfully uploaded.')
        return jsonify({'response': 'File successfully uploaded.'}), 200

    print(f'File extension {file.filename} not allowed.')
    return jsonify({'error': f'File extension {file.filename} not allowed.'}), 400

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/api/download_file', methods=['POST'])
def download_file():
    user_id = request.get_json().get('user_id')
    user_dir = os.path.join(app.config['UPLOAD_FOLDER'], user_id)
    if not os.path.exists(user_dir) or len(os.listdir(user_dir)) == 0:
        return jsonify({'error': 'File does not exist.'}), 400

    filepath = os.path.join(user_dir, os.listdir(user_dir)[0])

    if os.path.exists(filepath):
        return send_file(filepath, as_attachment=True)

    return jsonify({'error': 'Internal Server Error'}), 400


@app.route('/', methods=['GET'])
def test():
    return jsonify({'response': 'Hello World!'}), 200


if __name__ == "__main__":
    app.run(debug=DEBUG)

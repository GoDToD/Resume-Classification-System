from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['upload_folder'] = './uploaded_images'

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "API server is running"})

@app.route('/api/hello', methods=['GET'])
def hello_world():
    return jsonify({"message": "Hello, World!"})

@app.route('/api/upload_image', methods=['GET'])
def get_upload_image():
    return jsonify({"message": "Upload Image"})

@app.route('/api/upload_image', methods=['POST'])
def post_upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    file = request.files['resume']
    return jsonify({"message": "Recognised"})

if __name__ == '__main__':
    app.run(debug=True,port=7766)
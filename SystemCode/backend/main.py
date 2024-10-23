from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['upload_folder'] = './uploaded_images'

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "API server is running"})

@app.route('/api/upload_resume', methods=['POST'])
def post_upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    file = request.files['resume']
    return jsonify({"message": "Recognised"})

@app.route('/api/class_count', methods=['GET'])
def get_class_count():
    return jsonify({"message": "Pie chart data"})


if __name__ == '__main__':
    app.run(debug=True,port=7766)
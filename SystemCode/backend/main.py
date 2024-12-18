from flask import Flask, jsonify, request
from flask_cors import CORS
from services.utils import classify_resume, get_pdf_text

app = Flask(__name__)
CORS(app)
app.config['upload_folder'] = './uploaded_pdf'

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "API server is running"})

@app.route('/api/upload_resume', methods=['POST'])
def post_upload_resume():
    if 'resume' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    files = [request.files['resume']]
    
    results = classify_resume(files)
    
    # file.save(f"{app.config['upload_folder']}/{file.filename}")

    return jsonify({"message": "Recognised", "result": results})

@app.route('/api/class_count', methods=['GET'])
def get_class_count():
    return jsonify({"message": "Pie chart data"})

@app.route('/api/bulk_upload', methods=['POST'])
def post_bulk_upload():
    if 'resume' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    files = request.files.getlist('resume')

    results = classify_resume(files)

    return jsonify({"message": "Bulk upload successful", "result": results})

@app.route('/api/login', methods=['POST'])
def post_login():
    return jsonify({"message": "Login successful"})


if __name__ == '__main__':
    app.run(debug=True,port=7766)
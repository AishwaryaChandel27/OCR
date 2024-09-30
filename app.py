import os
import torch
from flask import Flask, request, jsonify
from utils import load_model, extract_text_from_image  # Ensure this matches

app = Flask(__name__)

# Load model and processor
model, processor = load_model()

# Create uploads directory if it doesn't exist
if not os.path.exists('./uploads'):
    os.makedirs('./uploads')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400

    file = request.files['image']
    file_path = f"./uploads/{file.filename}"
    file.save(file_path)

    # Extract text from the uploaded image
    extracted_text = extract_text_from_image(file_path, model, processor)

    return jsonify({"result": extracted_text})

if __name__ == '__main__':
    app.run(debug=True)

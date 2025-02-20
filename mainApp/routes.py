from app import app
from flask import jsonify, request
from file_handling import allowed_file, extract_text
import os
from ai import summarize_text
from werkzeug.utils import secure_filename

#signup login features about home

@app.route("/")
def home():
    return "Flask App Hosted"

@app.route("/summarize", methods=["POST"])
def summarize():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)

        # Extract text
        extracted_text = extract_text(filepath)
        if not extracted_text:
            return jsonify({"error": "Could not extract text"}), 400

        # Summarize using OpenAI
        summary = summarize_text(extracted_text)

        return jsonify({"summary": summary})

    return jsonify({"error": "Invalid file type"}), 400


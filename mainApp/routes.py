from app import app
from flask import jsonify, request, render_template
from file_handling import allowed_file, extract_text
import os
from ai import summarize_text
from werkzeug.utils import secure_filename

#signup login features about home

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/features")
def features():
    return render_template('features.html')

@app.route("/admin")
def admin():
    return render_template('admin.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/project")
def project():
    return render_template('project.html')

@app.route("/team")
def team():
    return render_template('team.html')

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

if __name__ == '__main__':
    app.run(debug=True)


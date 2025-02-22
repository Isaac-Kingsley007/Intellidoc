from app import app
from flask import jsonify, request, render_template, send_file, url_for
from file_handling import allowed_file, extract_text
import os
from ai import talkWithBot, summarize_text
from werkzeug.utils import secure_filename
from fileconv import get_file_extension, convert_document

#signup login features about home

#path Routes Works fine

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

#==== Path Routes End =====#

# File Handler Route

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

#=== file route end ===

# ChatBot Route

@app.route("/chat", methods = ['POST'])
def chat():
    print(request.form.get('message'))

    message = request.form.get('message','')
    file = request.files.get("file", None)
    convtype = request.form.get("conversion_type",'none')

    print("Conv Type ", convtype)

    if not file:

        response = talkWithBot(message)
        print(response)

        return jsonify({"type":"text","content":response})
    
    if not allowed_file(file.filename):
        return jsonify({"error":"Invalid File Type"}), 400
    
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(filepath)

    if convtype == 'none':

        extracted_text = extract_text(filepath)
        if not extracted_text:
            return jsonify({"error": "Could not extract text"}), 400
        
        summary = summarize_text(extracted_text)

        return jsonify({"type":"text","content":summary})
    

    fromext = get_file_extension(filename)

    output_file_name = "output." + convtype 

    outputfile_path = os.path.join(app.config["UPLOAD_FOLDER"], output_file_name)

    sucess = convert_document(filepath, outputfile_path, fromext, convtype)

    if not sucess:
        print('fail')
        return 'Conversion failed', 500
    
    res = send_file(
                outputfile_path,
                as_attachment=True,
                download_name="output." + convtype
    )

    file_url = url_for('static', filename="outputs/" + "output." + convtype)

    return jsonify({"type":"file", "content":file_url})
    


#== chatbot route ends ===

if __name__ == '__main__':
    app.run(debug=True)


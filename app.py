import os
from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename
import phishing_detection

app = Flask(__name__)
app.secret_key = "super_secret_key"
app.config['UPLOAD_FOLDER'] = "files"
ALLOWED_EXTENSIONS = {'txt', 'csv', 'html'}

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])
def home():
    url_result = None
    url_checked = None
    file_result = None
    file_checked = None

    if request.method == 'POST':
        # 1. Did the user use the URL Scanner?
        if 'url_name' in request.form:
            url_checked = request.form['url_name'].strip()
            if url_checked:
                url_result = phishing_detection.predict_phishing(url_checked)
            else:
                flash("Please enter a valid URL.")

        # 2. Did the user use the File Scanner?
        elif 'file' in request.files:
            file = request.files['file']
            if file.filename == '':
                flash('No file selected.')
            elif file and allowed_file(file.filename):
                try:
                    # Read the file and ignore weird characters
                    file_content = file.read().decode('utf-8', errors='ignore')
                    file_checked = file.filename
                    file_result = phishing_detection.analyze_file_content(file_content)
                except Exception as e:
                    flash("Error reading file. Make sure it is a text-based file.")
            else:
                flash("Invalid file type. Please upload .txt, .csv, or .html")

    return render_template("index.html", 
                           url_result=url_result, url=url_checked,
                           file_result=file_result, file_name=file_checked)

if __name__ == "__main__":
    app.run(debug=True)
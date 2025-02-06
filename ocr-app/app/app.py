from flask import Flask, request, render_template
import pytesseract
from PIL import Image
import os

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads/"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            return "No file part"
        
        file = request.files["file"]
        if file.filename == "":
            return "No selected file"

        # Save file
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(file_path)

        # Process OCR
        extracted_text = pytesseract.image_to_string(Image.open(file_path))

        return render_template("result.html", text=extracted_text)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

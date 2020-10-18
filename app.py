from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from upload_processor import process_geo_coder

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        csv_file = request.files['csv_file']
        csv_file.save(secure_filename("uploaded" + csv_file.filename))

        data_records = process_geo_coder("uploaded" + csv_file.filename)
        return render_template("index.html", text=data_records.to_html(), data="data_viewer.html")


@app.route("/download")
def download():
    pass


if __name__ == "__main__":
    app.run(debug=True)

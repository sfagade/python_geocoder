from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from upload_processor import process_geo_coder

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.context_processor
def get_current_user():
    print("context called", data_records)
    return {"data": data_records.to_html(classes='data')}


@app.route("/success", methods=['POST'])
def success():
    global data_records

    if request.method == 'POST':
        csv_file = request.files['csv_file']
        csv_file.save(secure_filename("uploaded" + csv_file.filename))

        data_records = process_geo_coder("uploaded" + csv_file.filename)
        return render_template("index.html", data="data_viewer.html")


@app.route("/download")
def download():
    pass

if __name__ == "__main__":
    app.run(debug=True)

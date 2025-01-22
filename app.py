from flask import Flask, render_template, request
import pandas as pd
from info_data import basic_data
import os

app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'Filecsv' not in request.files:
        return "No file part in the request", 400
    
    file = request.files['Filecsv']

    if file.filename == '':
        return "No file selected", 400
    
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    
    try:
        df = pd.read_csv(filepath)

        numeric_col, obj_col, basic_info_dic = basic_data(df)
        list_headers = list(basic_info_dic[next(iter(basic_info_dic))].keys())

        Data = df.head(10).to_html(classes='table table-striped table-bordered table-hover', index=False)
        Data = Data.replace('<thead>', '<thead class="table-dark">')


    except Exception as e:
        return f"Error reading CSV file: {str(e)}", 400
    
    # os.remove(filepath)

    return render_template(
        'info_data.html',
        Filename = file.filename,
        Data = Data,
        list_headers = list_headers,
        basic_info_dic = basic_info_dic,
    )



if __name__ == '__main__':
    app.run(debug=True)


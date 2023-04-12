import os
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'csv'}

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

filepath = None
df = None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            global filepath
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            global df
            df = pd.read_csv(filepath)
            row = df.iloc[0].to_dict()
            return render_template('index.html', row=row, row_index=0)
        else:
            return "無効なファイル形式です。CSVファイルをアップロードしてください。", 400

    return render_template('upload.html')

@app.route('/submit', methods=['POST'])
def submit():
    global df, filepath
    choice = request.form['choice']
    row_index = int(request.form['row_index'])
    df.at[row_index, 'choice'] = choice
    df.to_csv(filepath, index=False)

    next_index = row_index + 1
    if next_index < len(df):
        row = df.iloc[next_index].to_dict()
        return render_template('index.html', row=row, row_index=next_index)
    else:
        return "CSVファイルの処理が完了しました。"

@app.errorhandler(500)
def internal_server_error(error):
    return "サーバーエラーが発生しました。もう一度お試しください。", 500

if __name__ == '__main__':
    app.run(debug=True)

# CsvAnnotationHelper

CSVをドラッグアンドドロップすると、1行ずつ表示して、Yes/Noのボタンを押すと各行の末尾にYes/Noが追記されるだけの機能です。
ChatGPTなどに作成させたシナリオ素材などを人力で選別するために作りました。

Python（Flask）で動いています。ちなみにこのコードもChatGPTに大部分を作ってもらいました。

Apache Licence 2.0なのでお好きにお使いください。

インストール(Windows11のPowerShellでの例）
```
git clone https://github.com/matsuvr/CsvAnnotationHelper.git
cd CsvAnnotationHelper
python -m venv venv
.\venv\Script\activate
pip install flask
python .\app.py
```

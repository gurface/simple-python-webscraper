from flask import Flask, render_template, redirect, request, url_for
import requests
# from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def index():
    return render_template('index.html')

@app.route('/output', methods=["POST", "GET"])
def output():
    if request.method == 'POST':
        try:
            result = request.form['url_input']
            html_display = requests.get(result)
            return (html_display.text)
        except Exception:
            if (".com" in result) or (".co.uk" in result) or (".org" in result):
                html_display = requests.get(f'https://{result}')
                return html_display.text
            else:
                try:
                    return render_template(f'https://duckduckgo.com/q={result}')
                except Exception as ex:
                   return render_template('notfound.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    app.route('/teste')

@app.route('/teste')
def teste():
    with open('login.html', 'rb') as html:
        html = html.read()
    return html, 200
@app.route('/info.html')
def info():
    with open('info.html', 'rb') as html:
        html = html.read()
    return html, 200

if __name__ == '__main__':
    app.run(debug=True)
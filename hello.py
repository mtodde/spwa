from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Houston, we've had a problem"

#app.run(host='0.0.0.0') should not need this when launching with gunicorn
#app.run(host='0.0.0.0', port=80)












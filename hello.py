from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "It's Lunch time now!!!"

if __name__ == '__main__':
     app.run(host='0.0.0.0', --port=7500, debug=True)

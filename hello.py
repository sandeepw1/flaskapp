from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "It's Lunch time..empty stomach doesn't digest anything...especially study!!!"

if __name__ == '__main__':
     app.run(host='0.0.0.0', debug=True)

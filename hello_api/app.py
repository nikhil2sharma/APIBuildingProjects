from flask import Flask

app = Flask(__name__)  # creating application


@app.route('/')
def home():
    return 'Welcome first API'




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test')
def hello_world2():
    return 'Hello World2!'

if __name__ == '__main__':
    app.run()

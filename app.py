from flask import Flask

app = Flask(__name__)
'''Text'''

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World 2.0!'


if __name__ == '__main__':
    app.run()

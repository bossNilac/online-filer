import os
from flask import Flask
import app_config
from file_events import fileAction

app = Flask(__name__)


@app.route('/')
def hello():
    return os.listdir(os.getcwd())

@app.route('/text')
def text_test():
    fileAction (r'C:\Users\Emilia\PycharmProjects\online-filer\test.txt','nigger','w')
    return 'done'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=app_config.PORT, debug=True)
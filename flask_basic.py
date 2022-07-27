#####################GET###############################

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def add():
    a = request.args.get('a')
    b = request.args.get('b')
    return str(int(a)+int(b))

if __name__ == '__main__':
    app.run(port=8000)


#URL: http://127.0.0.1:8000?a=10&b=100
    


#####################POST###############################

from flask import Flask, request

app = Flask(__name__)

@app.route('/check', methods = ['POST'])
def add():
    a = request.form('a')
    b = request.form('b')
    return str(int(a)+int(b))

if __name__ == '__main__':
    app.run(port=8000)


#URL: http://127.0.0.1:8000/check

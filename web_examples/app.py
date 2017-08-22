from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    f=open("webdata","a")
    data = request.args['a']
    data="Getting data:"+data+"\n"

    f.write(data)
    f.close()
    return 'I got: a=' + request.args['a']

@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

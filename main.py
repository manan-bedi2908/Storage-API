from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 1;

@app.route('/image', methods=['GET','POST'])
def get_src():
    src =


@app.route('/shubhangi.com')
def data():
    return "hello"

if __name__ == '__main__':
    app.run(debug=True)

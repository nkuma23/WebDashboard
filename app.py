from flask import Flask




app = Flask(__name__)



@app.route('/')
@app.route('/home')
def home():
    return("<h1>Hello X1</h1>") 


@app.route('/control')
def control():
    return("<h2>This is the controls page. Expected in Winter 2021</h2>")
if __name__=="__main__":
    app.run(port=5005, debug=True)
from flask import Flask
import flask
app = Flask(__name__)

@app.route('/')
def hello_world():  
    return Flask.render_template('newuser.html', name="Please enter your info")


if __name__ == "__main__":
    app.run(debug=True)
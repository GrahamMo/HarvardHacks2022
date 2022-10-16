from flask import Flask
import flask
app = Flask(__name__)

@app.route('/')
def hello_world():  
    return flask.render_template('index.html', name="Please enter your info")


if __name__ == "__main__":
    # app = create_app()
    app.run(debug=True)
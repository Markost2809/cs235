from flask import Flask, render_template
from flask_login import *

app = Flask(__name__)

login_manager = LoginManager()


@app.route('/login')
def main():
    return render_template("Login.html")


if __name__ == '__main__':
    app.run(debug=True)

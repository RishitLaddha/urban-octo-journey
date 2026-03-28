from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Running on azure 🚀 CI/CD done by Rishit Laddha 2309575"

if __name__ == "__main__":
    app.run()

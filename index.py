from flask import Flask
concentrations = Flask(__name__)
@concentrations.route("/")
def run():
    return "Welcome to Aeris"

if __name__ == "__main__":
    concentrations.run(host="0.0.0.0", port=int("3000"), debug=True)
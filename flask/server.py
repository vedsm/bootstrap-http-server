from flask import Flask

app = Flask(__name__)

@app.route("/")
def root():
    return "This the root page :)"

@app.route("/health")
def health():
    return "The show is going well :D"

@app.route("/example")
def example():
    return "This is a sample API :3"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4200)

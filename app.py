from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello!"

# Routing
@app.route("/say-hi-to-dinara")
def hi():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()

from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return """
    <h2>Bye-Week Scout</h2>
    <form action="/echo" method="POST">
        <label>Type something:</label>
        <input name="user_input">
        <button type="submit">Submit</button>
    </form>
    """

@app.route("/echo", methods=["POST"])
def echo():
    text = request.form.get("user_input", "")
    return "You entered: " + text

if __name__ == "__main__":
    app.run()

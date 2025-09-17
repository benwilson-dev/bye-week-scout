from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.get("/")
def index():
    return """
    <h2>Bye-Week Scout</h2>
    <form action="/echo" method="POST">
      <label>Type something:</label>
      <input name="user_input" />
      <button type="submit">Submit</button>
    </form>
    """

@app.post("/echo")
def echo_post():
    text = request.form.get("user_input", "")
    return "You entered: " + text

@app.get("/echo")
def echo_get():
    return redirect(url_for("index"))
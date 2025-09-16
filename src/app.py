from flask import Flask, request

app = Flask(__name__)

@app.get("/")
def index():
    return """
    <h2>Bye-Week Scout </h2>
    <form action="/echo" method="POST">
      <label>Type something:</label>
      <input name="user_input">
      <button type="submit">Submit</button>
    </form>
    """

@app.post("/echo")
def echo():
    text = request.form.get("user_input", "")
    return "You entered: " + text
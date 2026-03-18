from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    name = "Shanon Mwangi"
    student_id = "S2561435"
    now = datetime.now()

    return f"""
    <h1>Cloud Computing and Web Services</h1>
    <h1>Coursework 1 - Diet 1</h1>
    <h2>Task1 </h2>
    <h3>App Engine app</h3>
    <p>Name: {name}</p>
    <p>Student ID: {student_id}</p>
    <p>Date and Time: {now}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
from flask import Flask

app = Flask(__name__)


@app.get("/")
def status():
    return {"status": "OK"}

from flask import Flask

app = Flask(__name__)


@app.get("/status")
def status():
    return {"status": "OK"}

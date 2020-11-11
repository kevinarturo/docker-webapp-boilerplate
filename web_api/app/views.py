from app import app


@app.route('/')
def main():
    return "hello from flask dockerized"
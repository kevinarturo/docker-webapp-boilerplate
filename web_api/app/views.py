from app import app


@app.route('/api')
def main():
    return "hello from flask dockerized change in production"

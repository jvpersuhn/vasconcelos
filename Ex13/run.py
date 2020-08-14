from Ex13 import app

if __name__ == "__main__":
    app = app.create_app()
    app.run(
        port=5000,
        host="localhost",
        debug=True
    )
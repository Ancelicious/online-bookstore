from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bookstore API Version 1"

@app.route("/books")
def books():
    return [
        {
            "id": 1,
            "title": "DevOps Handbook"
        },
        {
            "id": 2,
            "title": "Site Reliability Engineering"
        },
        {
            "id": 3,
            "title": "The Hobbit"
        },
        {
            "id": 4,
            "title": "The fellowship of the ring"
        },
        {
            "id": 5,
            "title": "The Two towers"
        },
        {
            "id": 6,
            "title": "The return of the king"
        }
    ]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
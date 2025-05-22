from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    try:
        response = requests.get("https://zenquotes.io/api/random", timeout=5)
        quote_data = response.json()[0]
        quote = quote_data["q"]
        author = quote_data["a"]
    except Exception as e:
        quote = "Failed to fetch quote."
        author = f"Error: {e}"

    return f"<h1>Quote of the Day</h1><p>\"{quote}\" — {author}</p>"

if __name__ == "__main__":
    app.run()

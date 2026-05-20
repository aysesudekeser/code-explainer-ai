from flask import Flask, render_template, request
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/explain", methods=["POST"])
def explain():

    code = request.json["code"]

    print(code)

    return {
        "response": "This code uses a loop/function and prints output."
    }


if __name__ == "__main__":
    app.run(debug=True)
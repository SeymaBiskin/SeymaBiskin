from flask import Flask, render_template, request, redirect
from utility.read_write_json import write_to_json
import json

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/index.html")
def main_page():
    return render_template("index.html")

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_json(data, "database.json")
        return render_template("/message_thank_you.html", name=data["email"])
    else:
        return "Something went wrong, try again!"
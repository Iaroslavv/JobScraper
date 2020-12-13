from flask import render_template, redirect, url_for, Blueprint, request
from app.job_seeker.forms import FillInForm
from app.scraping.scraper import get_records


users = Blueprint("users", __name__)


@users.route("/", methods=["GET", "POST"])
def index():
    form = FillInForm()
    site = request.form.get("websites")
    if request.method == "POST":
        if site == "Indeed.com":
            position = form.position.data
            location = form.location.data
            get_records(position, location)
            print("DONE!")
            return redirect(url_for("users.results"))
        else:
            print("NOT INDEED")
    return render_template("index.html", form=form)


@users.route("/results", methods=["GET"])
def results():
    return render_template("results.html")

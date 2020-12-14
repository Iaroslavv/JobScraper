from flask import render_template, redirect, url_for, Blueprint, request
from app.job_seeker.forms import FillInForm
from app.scraping.scraper import Indeed, StackOver
import tablib


users = Blueprint("users", __name__)


@users.route("/", methods=["GET", "POST"])
def index():
    form = FillInForm()
    site = request.form.get("websites")
    if request.method == "POST":
        if site == "Indeed.com":
            position = form.position.data
            location = form.location.data
            Indeed.get_records(position, location)
            return redirect(url_for("users.results_indeed"))
        else:
            print("STAACK")
            position = form.position.data
            location = form.location.data
            StackOver.get_records(position, location)
            return redirect(url_for("users.results_stack"))
    return render_template("index.html", form=form)


@users.route("/resultsindeed", methods=["GET"])
def results_indeed():
    dataset = tablib.Dataset()
    with open('jobs_indeed.csv') as f:
        dataset.csv = f.read()
    data = dataset.html
    return render_template("results.html", data=data)


@users.route("/resultsstack", methods=["GET"])
def results_stack():
    dataset = tablib.Dataset()
    with open('jobs_stackover.csv') as f:
        dataset.csv = f.read()
    data = dataset.html
    return render_template("results.html", data=data)

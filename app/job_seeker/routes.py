from app import app
from flask import render_template, redirect, url_for
from app.job_seeker.forms import FillInForm
from app.scraping.scraper import get_records


@app.route("/", methods=["GET", "POST"])
def index():
    form = FillInForm()
    if form.validate_on_submit():
        position = form.position.data
        location = form.location.data
        get_records(position, location)
        return redirect(url_for("results"))
    return render_template("index.html", form=form)


@app.route("/results", methods=["GET", "POST"])
def results():
    pass
from flask import Flask


app = Flask(__name__, instance_relative_config=True)
app.config.from_object("config.config")

from app.job_seeker import routes
from app.job_seeker.routes import users
app.register_blueprint(users)
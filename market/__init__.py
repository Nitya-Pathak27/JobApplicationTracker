from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.secret_key = "job_tracker_secret_key"


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "nityapathak2710@gmail.com"
app.config['MAIL_PASSWORD'] = "msefsrbqvsmsqbzt"
mail = Mail(app)

from routes import auth_routes
from routes import application_routes
import os
from flask import (Flask, render_template, request, url_for, app)
#from flaskext.mysql import MySQL
from flask_admin import Admin
from flask_admin.contrib.sqlamodel import ModelView
from flask_sqlalchemy import SQLAlchemy

import flask_admin as admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Lavina@123456@localhost/sys'
#db = SQLAlchemy(app)

admin = Admin(app)
app.run()

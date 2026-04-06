# -*- coding: utf-8 -*-
from flask import Flask, redirect, url_for
from flask_login import LoginManager, current_user
from backend.config import config
from backend.database import db, init_db
from backend.models.user import User
import os

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')
app.config.from_object(config['development'])

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from backend.routes import auth, dashboard
app.register_blueprint(auth.bp)
app.register_blueprint(dashboard.bp)

@app.route('/')
def index():
    return redirect(url_for('dashboard.index') if current_user.is_authenticated else url_for('auth.login'))

if __name__ == '__main__':
    os.makedirs('database', exist_ok=True)
    with app.app_context():
        init_db(app)
    print("🔥 SMOKED! ERP - http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)

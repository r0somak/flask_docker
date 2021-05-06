from flask import Flask, render_template, redirect
from datetime import datetime as dt

from application.forms import SaveDataForm
from application.config import Config

flask_app = Flask(__name__)
flask_app.config.from_object(Config)

@flask_app.route('/', methods=['GET', 'POST'])
def index():
    form = SaveDataForm()
    if form.validate_on_submit():
        with open("logs.txt", "a") as f:
            f.write(f"{dt.now().isoformat()}: {form.name.data} {form.surname.data}\n")

        return redirect('/')
    return render_template('index.html', form=form)

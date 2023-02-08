import random
from flask import (
    render_template,
    url_for,
    redirect,
    request,
    send_from_directory,
    make_response,
    abort,
    session,
    flash)
from app import app
from app.forms import ShareForm
from app.models import db, Secret

# Home route
@app.route('/')
@app.route('/index')
def index():
    form = ShareForm()
    return render_template('index.html', form=form)

# Hide 
@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/share', methods=['POST'])
def share():
    form = ShareForm()
    if form.validate_on_submit():
        secret = Secret()
        secret.name = form.name.data
        secret.confidante = form.confidante.data
        secret.message = form.secret.data
        random.seed(10)
        rand = random.random()
        secret.hash = hash(f"{form.secret.data}{form.confidante.data}{form.name.data}{rand}")
        db.session.add(secret)
        db.session.commit()
        return redirect(f"/secret/{secret.hash}")
    return render_template('index.html', form=form)

@app.route('/secret/<hash>')
def secret_page(hash):
    secret = db.one_or_404(db.select(Secret).filter_by(hash=hash))
    return render_template('secret.html', secret=secret, url=request.base_url)

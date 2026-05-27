from flask import render_template, session, redirect, request
from app.main import bp


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html', title='Ana Sayfa')


@bp.route('/set_language/<lang>')
def set_language(lang):
    if lang in ['tr', 'en']:
        session['lang'] = lang
    return redirect(request.referrer or '/')

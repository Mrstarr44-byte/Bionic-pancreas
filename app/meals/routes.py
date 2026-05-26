from flask import render_template, request, flash, redirect, url_for
from flask_babel import gettext as _
from flask_login import login_required
from app.meals import bp
from app import db
from app.models import MealPreset
from app.meals.forms import MealForm
from sqlalchemy import select


@bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = MealForm()

    if form.validate_on_submit():
        meal = MealPreset(
            name_tr=form.name_tr.data,
            name_en=form.name_en.data,
            carb_per_serving=form.carb_per_serving.data,
            gi_value=form.gi_value.data,
            category=form.category.data or None
        )
        db.session.add(meal)
        db.session.commit()
        flash(_('Yemek başarıyla eklendi'), 'success')
        return redirect(url_for('meals.index'))

    page = request.args.get('page', 1, type=int)
    per_page = 10

    pagination = db.paginate(
        select(MealPreset).order_by(MealPreset.id),
        page=page, per_page=per_page, error_out=False
    )
    meals = pagination.items

    return render_template(
        'meals/index.html', meals=meals,
        pagination=pagination, form=form
    )

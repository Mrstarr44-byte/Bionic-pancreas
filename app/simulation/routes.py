from flask import render_template, flash, redirect, url_for, session, request
from flask_login import login_required, current_user
from sqlalchemy import select, delete
from flask_babel import _
from app.translations import get_text
from app.simulation import bp
from app.simulation.forms import SimulationForm
from app.simulation.engine import SimulationEngine
from app import db
from app.models import SimulationLog, MealPreset


@bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = SimulationForm()
    meals = db.session.execute(select(MealPreset).order_by(MealPreset.id)).scalars().all()
    if form.validate_on_submit():
        # Opsiyonel alanların None gelme ihtimaline karşı 0.0 fallback
        result = SimulationEngine.calculate_new_bg(
            form.current_bg.data, form.carbs.data or 0.0, form.insulin.data or 0.0
        )

        # Simülasyon logunu kaydet
        log = SimulationLog(
            user_id=current_user.id,
            action_type="manual_simulation",
            value=result['new_bg'],
            glucose_before=form.current_bg.data,
            glucose_after=result['new_bg']
        )
        db.session.add(log)
        db.session.commit()

        lang = session.get('lang', 'tr')
        msg = get_text(lang, 'sim_result').format(bg=result['new_bg'], status=result['status'])
        flash(msg, "success")

        session['last_simulation_status'] = result['status']
        return redirect(url_for('simulation.index'))

    last_status = session.pop('last_simulation_status', None)
    return render_template('simulation/index.html', title='Simülasyon', form=form, last_status=last_status, meals=meals)

@bp.route('/reset_simulations', methods=['POST'])
@login_required
def reset_simulations():
    stmt = delete(SimulationLog).where(SimulationLog.user_id == current_user.id)
    db.session.execute(stmt)
    db.session.commit()
    flash(_('flash_history_cleared'), 'success')
    return redirect(url_for('simulation.index'))

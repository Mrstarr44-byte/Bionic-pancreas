from flask import render_template, flash, redirect, url_for, session
from flask_login import login_required, current_user
from app.simulation import bp
from app.simulation.forms import SimulationForm
from app.simulation.engine import SimulationEngine
from app import db
from app.models import SimulationLog

@bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = SimulationForm()
    if form.validate_on_submit():
        # Opsiyonel alanların (carbs, insulin) None gelme ihtimaline karşı 0.0 değeri fallback yapılır.
        result = SimulationEngine.calculate_new_bg(form.current_bg.data, form.carbs.data or 0.0, form.insulin.data or 0.0)
        
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
        
        flash(f"Tahmini Yeni Kan Şekeri: {result['new_bg']} mg/dL - Durum: {result['status']}", "success")
        
        session['last_simulation_status'] = result['status']
        return redirect(url_for('simulation.index'))
    
    last_status = session.pop('last_simulation_status', None)
    return render_template('simulation/index.html', title='Simülasyon', form=form, last_status=last_status)

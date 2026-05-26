from flask import render_template, flash, redirect, url_for
from flask_login import login_required
from app.simulation import bp
from app.simulation.forms import SimulationForm
from app.simulation.engine import SimulationEngine

@bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = SimulationForm()
    if form.validate_on_submit():
        result = SimulationEngine.calculate_new_bg(form.current_bg.data, form.carbs.data, form.insulin.data)
        flash(f"Tahmini Yeni Kan Şekeri: {result['new_bg']} mg/dL - Durum: {result['status']}", "success")
        return redirect(url_for('simulation.index'))
    return render_template('simulation/index.html', title='Simülasyon', form=form)

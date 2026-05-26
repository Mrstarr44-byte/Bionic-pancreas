from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Optional

class SimulationForm(FlaskForm):
    current_bg = FloatField('Mevcut Kan Şekeri (mg/dL)', validators=[
        DataRequired(),
        NumberRange(min=20, max=600, message='20 ile 600 arasında bir değer girin')
    ])
    carbs = FloatField('Karbonhidrat (gram)', default=0.0, validators=[
        Optional(),
        NumberRange(min=0, max=500)
    ])
    insulin = FloatField('İnsülin (Ünite)', default=0.0, validators=[
        Optional(),
        NumberRange(min=0, max=100)
    ])
    submit = SubmitField('Simüle Et')

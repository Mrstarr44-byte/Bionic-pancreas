from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Optional

FIELD_RENDER_KW = {"class": "form-control text-start", "placeholder": "Değer giriniz..."}


class SimulationForm(FlaskForm):
    current_bg = IntegerField(
        'Mevcut Kan Şekeri (mg/dL)', default=None,
        render_kw=FIELD_RENDER_KW,
        validators=[
            DataRequired(),
            NumberRange(min=20, max=600, message='20 ile 600 arasında bir değer girin')
        ]
    )
    carbs = IntegerField(
        'Karbonhidrat (gram)', default=None,
        render_kw=FIELD_RENDER_KW,
        validators=[
            Optional(),
            NumberRange(min=0, max=500)
        ]
    )
    insulin = IntegerField(
        'İnsülin (Ünite)', default=None,
        render_kw=FIELD_RENDER_KW,
        validators=[
            Optional(),
            NumberRange(min=0, max=100)
        ]
    )
    submit = SubmitField('Simüle Et')

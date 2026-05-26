from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, Optional
from flask_babel import lazy_gettext as _l


class MealForm(FlaskForm):
    name_tr = StringField(
        _l('Yemek Adı (TR)'),
        validators=[DataRequired(), Length(max=100)]
    )
    name_en = StringField(
        _l('Yemek Adı (EN)'),
        validators=[DataRequired(), Length(max=100)]
    )
    carb_per_serving = FloatField(
        _l('Porsiyon Karbonhidrat (g)'),
        validators=[DataRequired(), NumberRange(min=0, max=500)]
    )
    gi_value = IntegerField(
        _l('Glisemik İndeks'),
        validators=[DataRequired(), NumberRange(min=0, max=100)]
    )
    category = StringField(
        _l('Kategori'),
        validators=[Optional(), Length(max=50)]
    )
    submit = SubmitField(_l('Ekle'))

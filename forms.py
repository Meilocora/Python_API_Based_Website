from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField, SelectField
from wtforms.validators import DataRequired, NumberRange


class CreateHotelForm(FlaskForm):
    location_name = StringField("Name of the location", validators=[DataRequired()])
    checkin = DateField("Check-In", validators=[DataRequired()])
    checkout = DateField("Check-Out", validators=[DataRequired()])
    sort = SelectField("Sort by", choices=[("BEST_VALUE", "Best Value"), ("POPULARITY", "Traveller Ranking"), ("PRICE_LOW_TO_HIGH", "Price (low to high)"), ("DISTANCE_FROM_CITY_CENTER", "Distance to city centre")])
    rating = SelectField("Rating", choices=[("50", "5 rating and up"), ("40", "4 rating and up"), ("30", "3 rating and up"), ("20", "2 rating and up")])
    adults = IntegerField("Adults", render_kw={"value": 2}, validators=[DataRequired(), NumberRange(min=1, max=5)])
    rooms = IntegerField("Rooms", render_kw={"value": 1}, validators=[DataRequired(), NumberRange(min=1, max=5)])
    priceMin = IntegerField("Min Price", render_kw={"value": 0}, validators=[NumberRange(min=0, max=10000)])
    priceMax = IntegerField("Max Price", render_kw={"value": 100000}, validators=[NumberRange(min=0, max=100000)])
    submit = SubmitField("Search")
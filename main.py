from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap5

from keys import SECRET_KEY
from forms import CreateHotelForm
from requests_utils import request_hotels
from hotel import Hotel

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
Bootstrap5(app)

@app.route("/", methods=["GET", "POST"])
def home():
    form = CreateHotelForm()
    if form.validate_on_submit():
        location_name = form.location_name.data
        checkin = form.checkin.data.strftime("%Y-%m-%d")
        checkout = form.checkout.data.strftime("%Y-%m-%d")
        sort = form.sort.data
        rating = form.rating.data
        adults = form.adults.data
        rooms = form.rooms.data
        priceMin = form.priceMin.data
        priceMax = form.priceMax.data

        hotels_data = request_hotels(location_name=location_name, checkin=checkin, checkout=checkout, sort=sort, rating=rating, adults=adults, rooms=rooms, priceMin=priceMin, priceMax=priceMax)

        hotels = []
        for data in hotels_data:
            new_hotel = Hotel(id=data['id'], title=data['title'], info=data['secondaryInfo'], rating=data['bubbleRating'], provider=data['provider'], price=data['priceForDisplay'][1:]+data['priceForDisplay'][0], link=data['commerceInfo']['externalUrl'] , images=data['cardPhotos'])
            hotels.append(new_hotel)

        return render_template("hotels.html", hotels=hotels)
    return render_template("index.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
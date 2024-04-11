class Hotel():
    def __init__(self, id, title, info, rating, provider, price, link, images):
        self.id = id
        self.title = title
        self.info = info
        self.rating = rating
        self.provider = provider
        self.price = price
        self.link = link
        self.images = []
        self.fetch_images(images)

    def fetch_images(self, images):
        for image in images:
            self.images.append(image['sizes']['urlTemplate'].split("?")[0])
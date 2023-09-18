class Restaurant:
  def __init__(self, name, address, phone_number):
    self.name = name
    self.address = address
    self.phone_number = phone_number
    self.reviews = []
  def add_review(self, review):
    self.reviews.append(review)
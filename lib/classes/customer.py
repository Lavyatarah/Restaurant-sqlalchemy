from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship,sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from review import Review
from sqlalchemy import create_engine
class Customer:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.reviews = []
  def add_review(self, review):
    self.reviews.append(review)
Base = declarative_base()

# Create an SQLAlchemy engine
engine = create_engine('sqlite:///database.db')

# Create a Session class
Session = sessionmaker(bind=engine)

# Create a Session instance
session = Session()


class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True)
    rating = Column(Integer)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))


    def favorite_restaurant(self):
       
        highest_rating = -1
        favorite = None
        for review in self.reviews():
            if review.rating > highest_rating:
                highest_rating = review.rating
                favorite = review.restaurant()
        return favorite
    
    # Session = sessionmaker()
    

    def add_review(self, restaurant, rating):
        # Implement this method to create a new review for the restaurant
        new_review = Review(customer_id=self.id, restaurant_id=restaurant.id, rating=rating)
        Session.add(new_review)
        session.commit()

    def delete_reviews(self, restaurant):
    
        session.query(Review).filter(Review.customer_id == self.id, Review.restaurant_id == restaurant.id).delete()
        session.commit()

    def reviews(self):
        
        return session.query(Review).filter(Review.customer_id == self.id).all()

    def restaurants(self):
       
        reviewed_restaurants = set()
        for review in self.reviews():
            reviewed_restaurants.add(review.restaurant())
        return list(reviewed_restaurants)
  
  
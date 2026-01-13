class Restaurant:
    """A class of Restaurants and the food they serve"""

    def __init__(self, restaurant_name, cuisine_type):
        """Intialize instances of restaurants"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe the instance of the restaurant"""
        print(f"\nThe name of the restaurant is {self.restaurant_name.title()}.")
        print(f"They serve {self.cuisine_type.title()} as their main dish.")

    def open_restaurant(self):
        """Declare the restaurant as open!"""
        print(f"{self.restaurant_name.title()} is now open!")


fav_restaurant = Restaurant("Kada Fries", "Chicken and Chips")
your_fav_restaurant = Restaurant("Kilimanjaro", "Sharwama")
his_fav_restaurant = Restaurant("Home and Away", "Fried Rice")

list_of_favourite_restaurants = [fav_restaurant, your_fav_restaurant,
                                 his_fav_restaurant]

for fav_rest in list_of_favourite_restaurants:
    fav_rest.describe_restaurant()
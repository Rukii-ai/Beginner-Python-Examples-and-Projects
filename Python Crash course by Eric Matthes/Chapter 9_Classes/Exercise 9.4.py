class Restaurant:
    """A class of Restaurants and the food they serve"""

    def __init__(self, restaurant_name, cuisine_type):
        """Intialize instances of restaurants"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def set_number_served(self, number):
        """Set the number of customers served"""
        if number >= self.number_served:
            self.number_served = number
        elif number <= self.number_served:
            print("Number of customers served can not be rolled back!")

    def increment_number_served(self, number):
        """Increase number of customers served by given amount"""
        if number > 0:
            self.number_served += number
        elif number < 0:
            print("Please enter a valid number of customers served.")

    def describe_restaurant(self):
        """Describe the instance of the restaurant"""
        print(f"The name of the restaurant is {self.restaurant_name.title()}.")
        print(f"They serve {self.cuisine_type.title()} as their main dish.")

    def open_restaurant(self):
        """Declare the restaurant as open!"""
        print(f"{self.restaurant_name.title()} is now open!")


restaurant = Restaurant("Kada Fries", "Chicken and Chips")

print(restaurant.number_served)

restaurant.number_served = 5_128
print(restaurant.number_served)

restaurant.set_number_served(20_000)
print(restaurant.number_served)

restaurant.set_number_served(10_000)
print(restaurant.number_served)

restaurant.increment_number_served(200)
print(restaurant.number_served)

restaurant.increment_number_served(-500)
print(restaurant.number_served)

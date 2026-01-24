class Restaurant:
    """A class of Restaurants and the food they serve"""

    def __init__(self, restaurant_name, cuisine_type):
        """Intialize instances of restaurants"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe the instance of the restaurant"""
        print(f"The name of the restaurant is {self.restaurant_name.title()}.")
        print(f"They serve {self.cuisine_type.title()} as their main dish.")

    def open_restaurant(self):
        """Declare the restaurant as open!"""
        print(f"{self.restaurant_name.title()} is now open!")

class IceCreamStand(Restaurant):
    """Represent aspects of cuisines specific to icecreams"""

    def __init__(self, restaurant_name, cuisine_type, flavours):
        """Initialize instances of icecreams"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = flavours

    def describe_flavours(self):
        """Describe flavours available"""
        print("The flavours we have available are:")
        for flavour in self.flavours:
            print(flavour.title())


IceCreamStand_no_1 = IceCreamStand("Icecream World", "Icecream",
                                   ["vanilla", "chocolate", "strawberry", "banana"])

IceCreamStand_no_1.describe_flavours()

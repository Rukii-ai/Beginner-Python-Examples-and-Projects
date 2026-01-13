class User:
    """A class of user profiles"""

    def __init__(self, first_name, last_name, **user_profile):
        """Generate instances of the class Users"""

        name = f"{first_name} {last_name}"
        
        user_profile["first name"] = first_name
        user_profile["last name"] = last_name
        user_profile["name"] = name


        for key in user_profile:
            self.key = user_profile[key]

        self.user_profile = user_profile
        
        self.first_name = first_name
        self.last_name = last_name
        self.name = name
        
    def describe_user(self):
        """Provides all information about user profile"""
        print(f"\nBelow is a summary of each user's information:")

        for key in self.user_profile:
            print(f"\t{key.title()}: {self.user_profile[key].title()}")

    def greet_user(self):
        """For generating personalised greetings to each user"""
        print(f"Hello {self.name.title()} Welcome back!")

my_profile = User("stephen", "aguele", age="18", nationality="Nigerian",
                  occupation="student")
your_profile = User("jane", "anata", city="Lagos", age="19", fav_food="Rice")
his_profile = User("John", "doe")
her_profile = User("Martha", "Allen", school="University of Lagos")
their_son_profile = User("joseph", "Stan", status="Single", position="First")

user_list = [my_profile, your_profile, his_profile,
             her_profile, their_son_profile]

for profile in user_list:
    profile.describe_user()
    profile.greet_user()
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
        self.login_attempts = 0        
        self.first_name = first_name
        self.last_name = last_name
        self.name = name

    def increment_login_attempts(self):
        """Increases login attempts by 1 everytime a user logs in"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets login attempts to 0"""
        self.login_attempts = 0
        
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

my_profile.increment_login_attempts()
print(my_profile.login_attempts)

my_profile.increment_login_attempts()
print(my_profile.login_attempts)

my_profile.increment_login_attempts()
print(my_profile.login_attempts)

my_profile.increment_login_attempts()
print(my_profile.login_attempts)

my_profile.increment_login_attempts()
print(my_profile.login_attempts)

my_profile.reset_login_attempts()
print(my_profile.login_attempts)
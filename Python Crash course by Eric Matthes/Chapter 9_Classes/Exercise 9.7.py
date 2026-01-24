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



class Admin(User):
    """Model a special class of users known as admins"""

    def __init__(self, first_name, last_name, priviledges, **user_profile):
        """Initialize instances of the Admin class"""
        super().__init__(first_name, last_name, **user_profile)
        self.priviledges = priviledges

    def show_priviledges(self):
        """Display all admin priviledges"""
        print(f"The Admin user {self.name.title()} has the following priviledges:")
        for priviledge in self.priviledges:
            print(priviledge.title())


Admin_1 = Admin("Jack", "Robison", Marital_Status="Married", age=27,
                years_of_experience=7,
                priviledges=["can add post","can delete post", "can ban user",
                "can modify accounts", "can generate reports"])

Admin_1.show_priviledges()


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


class Priviledges():
    """Model the priviledges of an admin"""
    # I need to set prividelges to a value as a postional arguement
    # Or a keyword arguement or else the code won't run
    def __init__(self, priviledges=["can add post",
                                    "can ban user", "can generate reports"]):
        """Initialize intances of the priviledge class"""
        self.priviledges = priviledges

    def show_priviledges(self):
        """Display all admin priviledges"""
        print(f"This Admin user has the following priviledges:")
        for priviledge in self.priviledges:
            print(priviledge.title())


class Admin(User):
    """Model a special class of users known as admins"""

    def __init__(self, first_name, last_name, **user_profile):
        """Initialize instances of the Admin class"""
        super().__init__(first_name, last_name, **user_profile)
        self.list_of_admin_priviledges = Priviledges()


Admin_2 = Admin("Mary", "Sander", age=21, years_of_experience=2)


Admin_2.list_of_admin_priviledges.show_priviledges()


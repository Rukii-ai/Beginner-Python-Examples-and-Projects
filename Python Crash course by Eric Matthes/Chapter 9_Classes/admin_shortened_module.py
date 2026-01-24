"""A class that models an admin user"""

from user_module import User
from priviledges_module import Priviledges

class Admin(User):
    """Model a special class of users known as admins"""

    def __init__(self, first_name, last_name, **user_profile):
        """Initialize instances of the Admin class"""
        super().__init__(first_name, last_name, **user_profile)
        self.list_of_admin_priviledges = Priviledges()
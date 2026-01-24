"""A class that models admin Priviledges"""

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
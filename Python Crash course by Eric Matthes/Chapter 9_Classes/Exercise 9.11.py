import admin_module as am

admin_user = am.Admin('john_doe', 'johnson', location='USA', age="35",
                      years_of_experience="10")

admin_user.describe_user()
admin_user.list_of_admin_priviledges.show_priviledges()
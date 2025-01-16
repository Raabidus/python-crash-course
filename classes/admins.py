from users import Admin

martin_admin = Admin('pitomec', 'peša', 125, 105, 'female', 0)

martin_admin.privilages.show_privilages()

"""9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173).
Store the classes User, Privileges, and Admin in one module. Create a sepa-
rate file, make an Admin instance, and call show_privileges() to show that
everything is working correctly."""
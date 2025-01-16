"""9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173).
Store the classes User, Privileges, and Admin in one module. Create a sepa-
rate file, make an Admin instance, and call show_privileges() to show that
everything is working correctly."""

from user_module import User

class Privilages:
    def __init__(self):
        self.privilages = ["can add post", "can delete post", "can ban user"]

    def show_privilages(self):
        print(f"Admin privilages are {self.privilages}")

class Admin(User):
    def __init__(self, first_name, last_name, height, weight, body, login_attempts):
        super().__init__(first_name, last_name, height, weight, body, login_attempts)
        self.privilages = Privilages()



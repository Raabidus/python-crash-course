#Classes

"""Simple attempt to model a dog"""
class Dog:
    """Intiliaze name and age atributes"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        """Simulate dog is sitting"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate dog is rolling"""
        print(f"{self.name} rolled over")

my_dog = Dog("Alik", 6)
your_dog = Dog("Kikina", 9)

print(f"My dogs name is {my_dog.name}.")
print(f"My dog is {my_dog.age} old.")

print(f"Your dogs name is {your_dog.name}.")
print(f"Your dogs age is {your_dog.age}.")

my_dog.sit()
my_dog.roll_over()


your_dog.sit()
your_dog.roll_over()

"""
Try it yourself.
"""


"""9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indi-
cating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attri-
butes individually, and then call both methods."""

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
            print(f"Restaurants name is {self.restaurant_name}.")
            print(f"Restaurants couisine is {self.cuisine_type}.")

    def open_restaurant(self):
            print(f"Restaurant {self.restaurant_name} is open.")

    def set_number_served(self, customers):
         self.number_served = customers

restaurace = Restaurant("Kokoti", "Italská")

print(f"Restaurants name is {restaurace.restaurant_name}.")
print(f"Restaurants cuisine is {restaurace.cuisine_type}.")


"""9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
"""

restaurace_1 = Restaurant("Píčovina", "Česká")
restaurace_2 = Restaurant("Babička", "Japonská")
restaurace_3 = Restaurant("Kokotina", "Svahilská")

restaurace_1.describe_restaurant()
restaurace_2.describe_restaurant()
restaurace_3.describe_restaurant()


"""9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user."""

class User:
    def __init__(self,first_name, last_name, height, weight, body, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.height = height
        self.weight = weight
        self.body = body
        self.login_attempts = login_attempts
    
    def describe_user(self):
        print(f"Users name is {self.first_name} {self.last_name}")
        print(f"Users weight is {self.weight} adn heigt is {self.height}.")
        print(f"User is: {self.body}")

    def greet_user(self):
        print(f"Hello user {self.first_name} {self.last_name}")

    def increment_login_attemtps(self):
        self.login_attempts += 1
  

    def reset_login_attempts(self):
        self.login_attempts = 0


user_1 = User("Martin", "Král", "126cm", "76kg", "male", 0)

user_1.describe_user()
user_1.greet_user()


"""
T ry It Yourse l f
"""

"""
9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any num-
ber you like that could represent how many customers were served in, say, a
day of business.
"""

restaurace_4 = Restaurant("Indická", "Thajské jídlo")

print(f"Restaurace obsloužila: {restaurace_4.number_served}")
restaurace_4.set_number_served(666)

print(f"Po směně restaurace obsloužila: {restaurace_4.number_served} zákazníků.")


"""
9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 162). Write a method called increment_login
_attempts() that increments the value of login_attempts by 1. Write another
method called reset_login_attempts() that resets the value of login_attempts
to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.
"""

uživatel = User("Martin", "Novák", 176, 90, "male", 0)

uživatel.increment_login_attemtps()

print(f"Uživatel {uživatel.first_name} {uživatel.last_name} se přihlásitl {uživatel.login_attempts}.")

uživatel.reset_login_attempts()

print(f"Uživatel {uživatel.first_name} {uživatel.last_name} se prihlásil {uživatel.login_attempts}.")


# T ry It Yourse l f
"""
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method.
"""

class IceCreamsStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type,):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ["vanilka", "čokoláda", "jahoda"]

    def get_flavours(self):
         print(f"{self.restaurant_name} flavours are {self.flavours}.")

stanek_1 = IceCreamsStand("Zmrzka", "Italská")

stanek_1.get_flavours()

"""
9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method.
"""

class Privilages:
    def __init__(self):
        self.privilages = ["can add post", "can delete post", "can ban user"]

    def show_privilages(self):
        print(f"Admin privilages are {self.privilages}")

class Admin(User):
    def __init__(self, first_name, last_name, height, weight, body, login_attempts):
        super().__init__(first_name, last_name, height, weight, body, login_attempts)
        self.privilages = Privilages()

administrator_1 = Admin("pepa", "novak", 120, 390, "male", 0)


     

"""
9-8. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.
(continued)
"""

administrator_2 = Admin("martin", "pičus", 111, 99, "female", 1)
administrator_2.privilages.show_privilages()


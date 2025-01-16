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
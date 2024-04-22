class UserManager:
    def __init__(self):
        self.user_list = []
        self.counter = 0


    def generate_id(self):
        self.counter += 1
        return self.counter

    

    def create_a_user(self, name, password, user_type):
        new_user_id = self.generate_id()
        new_user = User(new_user_id, name, password, user_type)
        self.user_list.append(new_user)



    def find_users(self, ids):
        users_found = []
        for user in self.user_list:
            if user.user_id in ids:
                users_found.append(user)

        return users_found



class User:
    def __init__(self, user_id: int, name: str, password: str, user_type: str):
        self.user_id = user_id
        self.name = name
        self.password = password
        self.user_type = user_type

    

    def __str__(self):
        return f"ID: {self.user_id}, name: {self.name}, type: {self.user_type}"

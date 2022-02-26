class User:
    def __init__(self, first_name, last_name, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    def get_full_username(self):
        return self.first_name + ' ' + self.last_name


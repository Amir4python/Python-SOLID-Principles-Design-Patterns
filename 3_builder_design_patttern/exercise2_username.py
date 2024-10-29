
class User:
    def __init__(self):
        self.firstname = None
        self.lastname = None
        self.email = None
        self.age =None
        self.phone =None

    @property
    def get_firstname(self):
        return self.firstname
    @property
    def get_lastname(self):
        return self.lastname

    @property
    def get_password(self):
        return self.lastname

    @property
    def get_email(self):
        return self.email

    @property
    def get_age(self):
        return self.age

    @property
    def get_phone(self):
        return self.phone



    def set_firstname(self, firstname):
        self.firstname = firstname
    def set_lastname(self, lastname):
        self.lastname = lastname

    def set_password(self, lastname):
        self.lastname = lastname

    def set_email(self, email):
        self.email = email

    def set_age(self, age):
        self.age = age

    def set_phone(self, phone):
        self.email = phone

class UserBuilder:
    def __init__(self):
        self.user = User()



    def set_firstname(self, firstname):
        self.user.set_firstname(firstname)
    def set_lastname(self, lastname):
        self.user.set_lastname(lastname)
    def set_password(self, password):
        self.user.set_password(password)
    def set_email(self, email):
        self.user.set_email(email)
    def set_age(self, age):
        self.user.set_age(age)
    def set_phone(self, phone):
        self.user.set_phone(phone)
    def get_user(self):
        return self.user


if __name__ == '__main__':


    builder = UserBuilder()
    builder.set_firstname('John')
    builder.set_lastname('Doe')
    builder.set_password('password')
    builder.set_email('zrYnH@example.com')


    user = builder.get_user()
    print(user.firstname)
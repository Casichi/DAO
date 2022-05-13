class User:

    def __init__(self, name, password):
        self._name = name
        self._password = password

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    def __str__(self):
        return f'User: Name {self._name}, Password {self._password}'


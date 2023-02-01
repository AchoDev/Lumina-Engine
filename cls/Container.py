
class Container:
    def __init__(self, value=None):
        self.value = value

    def change(self, new_value):
        self.value = new_value

    def add_number(self, value):
        self.value += value
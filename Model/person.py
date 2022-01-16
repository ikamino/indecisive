class Person:
    price_range = 0 # one of [1]
    location = '' # address 
    # feeling = '' # a word out of a list of possible choices
    name = '' 
    age = 0
    num_of_people = 0

    def __init__(self, name, age, price_range, location, num_people):
            # Assign the argument to the instance's name attribute
            self.name = name
            # self.feeling = feeling
            self.location = location
            self.price_range = price_range
            self._age = age
            self.num_of_people = num_people

    

    
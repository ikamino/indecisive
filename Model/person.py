class Person:
    price_range = 0 # one of [1]
    location = '' # address 
    feeling = '' # a word out of a list of possible choices
    name = '' #

    def __init__(self, name, price_range, location, ):
            # Assign the argument to the instance's name attribute
            self.name = name
            
            # Initialize property
            self._age = 0
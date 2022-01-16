class Person:
    price_range = 0 # one of [1]
    location = '' #
    feeling = ''
    name = ''

    def __init__(self, name, price_range, location, ):
            # Assign the argument to the instance's name attribute
            self.name = name
            
            # Initialize property
            self._age = 0
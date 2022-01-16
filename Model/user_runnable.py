from person import Person
persons = []
running = 1
def init():
    global running
    print("Welcome to indecisive, a program designed to help you places to eat near you, depending on how you feel!")
    running = 1
    

    while running: 
        menu(running)
   


def menu(): 
    print('Please input what you would like to do. Type \t help \t to get a list of commands')

    user_input = input() 
    user_input.lower
    # commands(user_input)
    commands(user_input)


def commands(user_input): 
    if user_input == "help": 
        help()
    elif user_input == "decisions":
        decisions()

    elif user_input == "exit": 
        exit_program()

def help():
    print('Here are the available functions to you \nhelp: display commands \ndecisions: go through the steps to satisfy your cravings for the day. \n exit: exit the program')
    

def exit_program():
    global running
    running = 0



def decisions(): 
    print("We're glad to help you find what to eat, and where, near you!")
    if check_profile(): 
        print("Just to get to know you better, we'd like to ask you some questions!")
        p1 = create_profile()
        print("If at any time you'd like to change information, just let us know through the 'change' command!")


# is there already a profile init? 
def check_profile(): 
    if persons: 
        return 0
    else: 
        return 1


def create_profile(): 
    print("What's your name?")
    name = input()
    print("How old are you?")
    age = input()
    print("From a scale of 1-3 whats your price range?")
    address = input("Street Address? ")
    city = input("city? ")
    province = input("province? ")
    num_people = input("how many people you with?")



# after creating profile put profile into persons list -- doesnt have to be large just needed a way to track instances globally. 
# from there, start questionaire on feelings and fill out feelings_sort.py.
#whatever result we get from feelings_sort.py match up with factors such as age and (need gender in persons.py as well) (ie according to x study girls like ice cream more while guys like home-cooked meals like roast beef more. )

# after all of that its just connecting to google apis... shouldn't need too many difficult packages. If we have time implement a left right system based on lists filled with words that suggest certain emotions, or different cuisines/food types.




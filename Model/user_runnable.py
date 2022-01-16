from person import Person

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
    p = Person()


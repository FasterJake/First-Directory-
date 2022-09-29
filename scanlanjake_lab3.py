"""Program that ask the user to make a selection of something to do, as in to
 see all the 50 states in order with their data, select a specific state and
 obtain its data as well as a picture of the state flower. Get the 5 most populous
 states and graph the data, as well as manipulate and change a states population"""

# Imports to import functions of matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Statement to welcome user into my program
print("Welcome to my state altering program!")


def menu():
    """Function menu() to create and print out the menu selections for the different options"""
    # Asks user to make a selection from given options
    print("\n[1] Display all the states in alphabetical order with all info.\n"
          "[2] Find a specific state and print all that states info.\n"
          "[3] Create a graph of the 5 most populated states.\n"
          "[4] Update a chosen states population.\n"
          "[5] Exit\n")


# Dictionary states{}, which holds the key of the state name which holds values
# of capital key which holds the value of the capital, population key which holds
# value of number of people, and flower key that holds the state flower name


states = {
    "Alabama": {"Capital": "Montgomery", "Population": 4918689, "Flower": "Camellia"},
    "Idaho": {"Capital": "Boise", "Population": 1823594, "Flower": "Syringa"},
    "Missouri": {"Capital": "Jefferson City", "Population": 6153233, "Flower":
        "White Hawthorn Blossom"},
    "North Dakota": {"Capital": "Bismarck", "Population": 766044, "Flower": "Wild Prairie Rose"},
    "Louisiana": {"Capital": "Baton Rouge", "Population": 4637898, "Flower": "Magnolia"},
    "South Carolina": {"Capital": "Columbia", "Population": 5213272, "Flower": "Yellow Jessamine"},
    "New Mexico": {"Capital": "Santa Fe", "Population": 2100917, "Flower": "Yucca"},
    "Massachusetts": {"Capital": "Boston", "Population": 6902371, "Flower": "Mayflower"},
    "Illinois": {"Capital": "Springfield", "Population": 12620571, "Flower": "Violet"},
    "Georgia": {"Capital": "Atlanta", "Population": 10723715, "Flower": "Cherokee Rose"},
    "Colorado": {"Capital": "Denver", "Population": 5826185, "Flower": "Rocky Mountain Columbine"},
    "North Carolina": {"Capital": "Raleigh", "Population": 10594553, "Flower": "Dogwood"},
    "Connecticut": {"Capital": "Hartford", "Population": 3559054, "Flower": "Mountain Laurel"},
    "Alaska": {"Capital": "Juneau", "Population": 727951, "Flower": "Alpine Forget-me-not"},
    "Minnesota": {"Capital": "Saint Paul", "Population": 5673015, "Flower":
        "Pink and White Lady Slipper"},
    "Nevada": {"Capital": "Carson City", "Population": 3132971, "Flower": "Sagebrush"},
    "West Virginia": {"Capital": "Charleston", "Population": 1780003, "Flower": "Rhododendron"},
    "Arkansas": {"Capital": "Little Rock", "Population": 3025875, "Flower": "Apple Blossom"},
    "Florida": {"Capital": "Tallahassee", "Population": 21711157, "Flower": "Orange Blossom"},
    "New Hampshire": {"Capital": "Concord", "Population": 1365957, "Flower": "Purple Lilac"},
    "Maryland": {"Capital": "Annapolis", "Population": 6055558, "Flower": "Black-Eyed Susan"},
    "Pennsylvania": {"Capital": "Harrisburg", "Population": 12803056, "Flower": "Mountain Laurel"},
    "Oklahoma": {"Capital": "Oklahoma City", "Population": 3973707, "Flower": "Oklahoma Rose"},
    "Mississippi": {"Capital": "Jackson", "Population": 2971278, "Flower": "Coreopsis"},
    "Tennessee": {"Capital": "Nashville", "Population": 6886717, "Flower": "Tennessee Coneflower"},
    "Michigan": {"Capital": "Lansing", "Population": 9989642, "Flower": "Apple Blossom"},
    "Vermont": {"Capital": "Montpelier", "Population": 623620, "Flower": "Red Clover"},
    "Rhode Island": {"Capital": "Providence", "Population": 1060435, "Flower": "Violet"},
    "Washington": {"Capital": "Olympia", "Population": 7705917, "Flower": "Coast Rhododendron"},
    "South Dakota": {"Capital": "Pierre", "Population": 890620, "Flower": "American Pasque"},
    "Kansas": {"Capital": "Topeka", "Population": 2915269, "Flower": "Wild Native Sunflower"},
    "Oregon": {"Capital": "Salem", "Population": 4253588, "Flower": "Oregon Grape"},
    "Kentucky": {"Capital": "Frankfort", "Population": 4474193, "Flower": "Goldenrod"},
    "California": {"Capital": "Sacramento", "Population": 39562858, "Flower": "California Poppy"},
    "Arizona": {"Capital": "Phoenix", "Population": 7399410, "Flower": "Saguaro Cactus Blossom"},
    "Delaware": {"Capital": "Dover", "Population": 982049, "Flower": "Peach Blossom"},
    "Indiana": {"Capital": "Indianapolis", "Population": 6768941, "Flower": "Peony"},
    "Maine": {"Capital": "Augusta", "Population": 1349367, "Flower": "White Pine Cone"},
    "Wisconsin": {"Capital": "Madison", "Population": 5837462, "Flower": "Wood Violet"},
    "Nebraska": {"Capital": "Lincoln", "Population": 1943202, "Flower": "Goldenrod"},
    "Iowa": {"Capital": "Des Moines", "Population": 3161522, "Flower": "Wild Rose"},
    "New Jersey": {"Capital": "Trenton", "Population": 8878355, "Flower": "Violet"},
    "Virginia": {"Capital": "Richmond", "Population": 8569752, "Flower": "American Dogwood"},
    "Wyoming": {"Capital": "Cheyenne", "Population": 579917, "Flower": "Indian Paintbrush"},
    "Ohio": {"Capital": "Columbus", "Population": 11701859, "Flower": "Red Carnation"},
    "Texas": {"Capital": "Austin", "Population": 29363096, "Flower": "Bluebonnet"},
    "Utah": {"Capital": "Salt Lake City", "Population": 3258366, "Flower": "Sego Lily"},
    "New York": {"Capital": "Albany", "Population": 19376771, "Flower": "Rose"},
    "Montana": {"Capital": "Helena", "Population": 1076891, "Flower": "Bitterroot"},
}


def print_state_info():
    """Function to print all the states and their data in alphabetical order"""
    # For every state and its values, sorts all items inside the state dictionary
    for key, value in sorted(states.items()):
        # Prints state and separates it from values with a ":"
        print(key, ':', value)


def find_state():
    """Function to find a specific state and its information along with an image of state flower"""
    # Sets capitalized to false
    capitalized = False
    # While capitalized is not false, runs through the loop
    while not capitalized:
        # Asks user which state they would like info for and stores in key
        key = input("Which state would you like information for? Enter with capital: \n")
        # Checks to see if key's first letter is upper case
        if key[0].isupper():
            # If upper case, capitalized is true
            capitalized = True
            # If key is found in states dictionary
            if key in states:
                # Tells the user what they searched for and prints the state with its values
                print("You have searched for: ", key, ", ", states[key])
                # Uses matplotlib to read from a file, stores in img. Reads through the file path
                # and uses the users input to finish the file path to produce an image of flower
                img = mpimg.imread(f"Flower Images/{key}.jpg")
                # Draws the image
                plt.imshow(img)
                # Displays the image
                plt.show()
        # If capitalized is false, prints statement and runs through loop again
        else:
            print("Please make sure you enter a state with a capital letter!\n")


def population_graph():
    """Function to find the 5 most populous states and graph them"""
    # Creates max_values, runs through sorted states, creates a function for one time use
    # (lambda), calls it s. Gets the states list, checks the populations for highest, stores
    # the state in max_values, doesn't put the population number in and does this 5 times but
    # sets them to be in reverse order, so they are in descending order from high to low
    max_values = (sorted(states, key=lambda s: states[s].get("Population", 0), reverse=True)[:5])
    # Creates state_list to store populations
    state_list = []
    # Runs through each item in max_values
    for n in range(len(max_values)):
        # Prints each state name in order from greatest to least
        print(max_values[n])
        # assigns the max_values and data to state_name
        state_name = max_values[n]
        # Prints the data for each state in max_values and also prints its population
        print(states[state_name]["Population"])
        # Adds them to the state_list[]
        state_list.append(states[state_name]["Population"])
    # Puts max_values(state) on x-axis and state_list(populations) on y-axis
    plt.bar(max_values, state_list)
    # Labels y axis populations
    plt.ylabel("populations")
    # Labels x axis states
    plt.xlabel("states")
    # Adds a title
    plt.title("States with highest populations")
    # Displays the graph
    plt.show()


def population_alter():
    """Function to update or change the population of a chosen state"""
    # Sets is_string to false
    is_string = False
    # While is_string is not false, start loop
    while not is_string:

        # Asks user which state they would like to update
        pop_update = input("Which state would you like to update?\n")
        # If pop_update is a string and has an upper case letter, progresses through loop
        if pop_update.isalpha() and pop_update[0].isupper():
            # If statement is met, is_string is true
            is_string = True
            # Creates variable chosen_state to get and hold the state the user asked for
            chosen_state = states.get(pop_update)
            # Prints chosen_state
            print(chosen_state, "\n")
            # Nested while to loop while is_string is true
            while is_string is True:
                # Tries statements to progress loop
                try:
                    # Asks user how many people they want to add to the states population
                    amount = int(input("How many persons would you like to add to the population?\n"))

                    # Tries statements to progress loop
                    try:
                        # Asks user for the original amount because the program forgot
                        original = int(input("Please enter the original population.\n"))
                        print("Awesome we've got numbers!\n")

                        # Creates final_amount variable and subtracts amount from the original amount
                        final_amount = original + amount
                        # Updates the chosen_state in the list with the new amount
                        chosen_state.update({"Population": final_amount})
                        # Prints the updated info
                        print("The updated info for " + pop_update + " is: ", chosen_state)
                        break
                        # If not a number prints following statement and runs loop
                    except ValueError:
                        print("Welp, lets try this whole thing again, shall we, with a number?\n")

                # If not a number prints following statement and runs loop
                except ValueError:
                    print("We need actual numbers please get it together.\n")
        # If input is not a string or has a capital letter in the front or both, runs through loop
        else:
            print("Please enter the name of a state with a capital...\n")


# Sets selection to 0
selection = 0
# While selection is not 5, continue loop
while selection != 5:
    try:
        # Calls menu function
        # Asks user to make a selection
        # Starts while loop
        menu()
        selection = int(input("Please make a selection.\n"))
        # If selection is 1 calls print_state_info function
        if selection == 1:
            print_state_info()
        # if selection is 2 calls findState function
        elif selection == 2:
            find_state()
        # If selection is 3 calls populationGraph function
        elif selection == 3:
            population_graph()
        # If selection is 4 calls populationAlter function
        elif selection == 4:
            population_alter()
        elif selection == 5:
            # Says goodbye, and thanks user for using program
            print("Goodbye and thank you for using my program for world domination!")
    # If input is not a number, prints statement and runs loop
    except ValueError:
        print("We need numbers here, C'mon now!\n")
        # When user is asked to make another selection and runs a nested try to
        # be sure that a number is entered
        try:
            # Calls function to print menu
            #  Asks user if they would like to make another selection
            selection = int(input("Would you like to make another selection?\n"))
            # If selection is 1 calls print_state_info function
            if selection == 1:
                print_state_info()
            # if selection is 2 calls findState function
            elif selection == 2:
                find_state()
            # If selection is 3 calls populationGraph function
            elif selection == 3:
                population_graph()
            # If selection is 4 calls populationAlter function
            elif selection == 4:
                population_alter()
            # If selection is 5, exits the while loop
            if selection == 5:
                # Says goodbye, and thanks user for using program
                print("Goodbye and thank you for using my program for world domination!")
        # If input is not a number, prints statement, and enters back into the loop
        except ValueError:
            print("The numbers are at the door, please get it..\n")

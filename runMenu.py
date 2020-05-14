from lookup import UPC_lookup
from editBook import Edit_book

def Run_Menu():
    print("")
    print("======================")
    print("Welcome to the Pibrary")
    print("======================")
    print("")
    print("Please select from the following options")
    print("  (1) Check out/in a book")
    print("  (2) Edit a book")
    selection = input("Select a number and press enter: ")
    print("")
    print("")
    if(selection == "1"):
        UPC_lookup("J41G78S1608A06JH")
    elif(selection == "2"):
        Edit_book()
    elif(selection == "3"):
        print("Do something with the third option")
        #Search Books!
    else:
        print("Hey! You didn't select a valid option")

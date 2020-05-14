import json

def Edit_book():
    # Find the book we want to edit
    # scan the barcode
    scannedBarcode = "J41G78S1608A06JH"
    # search the database for the barcode
    with open('db.json', "r+") as db:
        books = json.load(db)
        foundBook = False
        for book in books:
            if(book['barcode'] == scannedBarcode):
                # Ask the user what they want to edit
                print("Please select what you would like to edit")
                print(" (1) Title")
                print(" (2) Author")
                print(" (3) Genre")
                print(" (4) Publish Date")
                print(" (5) Status")
                print("")
                selection = input("Select a number and press enter: ")
                goodSelection = False
                if(selection == "1"):
                    # Edit title
                    goodSelection = True
                    Update_Database_Field("title", "title", book)
                elif(selection == "2"):
                    # Edit author
                    goodSelection = True
                    Update_Database_Field("author", "author", book)
                elif(selection == "3"):
                    # Edit genre
                    goodSelection = True
                    Update_Database_Field("genre", "genre", book)
                elif(selection == "4"):
                    # Edit publishDate
                    goodSelection = True
                    Update_Database_Field("publish date", "publishDate", book)
                elif(selection == "5"):
                    # There are two options
                    goodSelection = True
                    print("Please select what you would like the status to be")
                    print(" (1) In")
                    print(" (2) Out")
                    statusInput = input("Type either 1 or 2 then hit enter: ")
                    # Either the book is In
                    if(statusInput == "1"):
                        book["status"] = "In"
                    # Or the book is Out
                    elif(True):
                        book["status"] = "Out"


                if(goodSelection):
                    #save file
                    db.seek(0)
                    json.dump(books, db, indent=4)
                    db.truncate()
                    print("Your edit was successful!")
                else:
                    print("You didn't select a valid option silly goose")


def Update_Database_Field(prettyText, dbText, book):
    current = ""
    if dbText in book:
        current = book[dbText]
    print("The current " + prettyText + " is: " + str(current))
    book[dbText] = input("What is the brand new " + prettyText + ": ")



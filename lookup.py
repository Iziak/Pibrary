import json

def UPC_lookup(upc):

    with open('db.json', "r+") as db:
        books = json.load(db)
        for book in books:
            if(book['barcode'] == upc):
                current_status = book['status']
                print("Current status is " + current_status)
                #change status
                #print new status
                #save file
            else:
                print(False)
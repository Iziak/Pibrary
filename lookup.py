import json

def UPC_lookup(upc):

    with open('db.json', "r+") as db:
        books = json.load(db)
        for book in books:
            if(book['barcode'] == upc):
                #print current status
                print("Current status is " + book['status'])
                #change status
                if(book['status'] == 'In'):
                    book['status'] = 'Out'
                else:
                    book['status'] = 'In'
                #print new status
                print("New status: " + book['status'])
                #save file
                db.seek(0)
                json.dump(books, db, indent=4)
                db.truncate()
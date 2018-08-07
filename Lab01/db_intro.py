from pymongo import MongoClient

mongo_uri = "mongodb://c4e20-lab-dbuser:jessemac87@ds033297.mlab.com:33297/c4e20-lab"

#1. Connect to database
client = MongoClient(mongo_uri)

#2. Get database
db = client.get_default_database()

#3. Create a collection
games = db["games"]

# #4. Create a document
# new_game = {
#     "title" : "TC",
#     "description" : "Trivia Crack"
# }

# #5. Insert document into collection
# games.insert_one(new_game)

#6. Read all documents
all_game = games.find()
first_game = all_game[0]
print(first_game["title"])
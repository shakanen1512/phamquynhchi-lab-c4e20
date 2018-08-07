from pymongo import MongoClient
mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)
db = client.get_default_database()

posts = db["posts"]

new_post = {
    "title" : "If you love Japan",
    "author" : "shakanen",
    "content" : """
    Don't stop at popular culture.
    Dive for its history.
    In its darkest moments you will find irony.
    In its maddest hours you will encounter change.
    For Japan is not reductive interpretation of good or evil.
    Japan is, simply put, the land of the rising sun.

    ~ by me, self-proclaimed Meiji historian
    """
}

posts.insert_one(new_post)
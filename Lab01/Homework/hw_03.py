from pymongo import MongoClient
mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)
db = client.get_default_database()

customers = db["customers"]
all_customers = customers.find()

count_1 = 0
count_2 = 0
count_3 = 0

for item in all_customers:
    events_is_true = False
    if item["ref"] == "events":
        events_is_true = True
    wom_is_true = False
    if item["ref"] == "wom":
        wom_is_true = True
    ads_is_true = False
    if item["ref"] == "ads":
        ads_is_true = True

    if events_is_true:
        count_1 += 1
    if wom_is_true:
        count_2 += 1
    if ads_is_true:
        count_3 += 1

import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot

labels = ["Event", "Word of Mouth", "Advertisements"]
values = [count_1, count_2, count_3]
colors = ["red", "yellow", "green"]

pyplot.pie(
    values, 
    labels=labels, 
    colors=colors,
    autopct='%1.1f%%'
)
pyplot.axis("equal")
pyplot.show()
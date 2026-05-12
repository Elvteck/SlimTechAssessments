import pymongo
from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://elvisugboaja85:Chime9426+@database-testing.bvtc26g.mongodb.net/?appName=Database-Testing")
db = cluster["Linkedin"]
collection = db ["User Posts"]
post1 = {"_id" : "Elvis", "caption": "Miva is a wonderful school structure"}
post2 = {"_id" : "Jeffery", "caption": "I just completed my 30 days journey on Google data analytics"}

comment1 = {"_id" : "Chidi", "post_id": "Elvis", "text": "That is so true" }
comment2 = {"_id": "David", "post_id": "Elvis", "text": "True. A rewarding school structure matters"}

comment1 = {"_id": "Google", "post_id": "Jeffery", "text": "Congrats Jeffery 'smile emoji' "}
comment2 = {"_id": "Stephanie", "post_id": "Jeffery", "text": "Congratulations"}


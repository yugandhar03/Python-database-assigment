import pymongo

def get_database_connection():
  client = pymongo.MongoClient("mongodb+srv://yugandhar:7032292232@mydatabase.i6jal.mongodb.net/?retryWrites=true&w=majority")
  db = client.test
  return db
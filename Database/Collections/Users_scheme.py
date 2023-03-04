from pymongo import MongoClient, ASCENDING

client = MongoClient('localhost', 27017)
db = client["Circles"]
users_collection = db["users"]
users_collection.create_index([("email", ASCENDING)], unique=True)
users_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["name", "surname", "email", "password", "created_at", "updated_at"],
        "properties": {
            "_id": {"bsonType": "objectId"},
            "name": {"bsonType": "string"},
            "surname": {"bsonType": "string"},
            "email": {
                "bsonType": "string",
                "pattern": "^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$",
            },
            "password": {"bsonType": "string"},
            "created_at": {"bsonType": "date"},
            "updated_at": {"bsonType": "date"},
        },
    }
}
users_collection = db.create_collection("users", validator=users_validator)



from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['Circles']

# Валидация для коллекции refUserRate
ref_user_rate_validator = {
    '$jsonSchema': {
        'bsonType': 'object',
        'required': ['user_id', 'rated_user_id', 'rating', 'created_at', 'updated_at'],
        'properties': {
            '_id': {
                'bsonType': 'objectId'
            },
            'user_id': {
                'bsonType': 'objectId'
            },
            'rated_user_id': {
                'bsonType': 'objectId'
            },
            'rating': {
                'bsonType': 'number',
                'minimum': 0,
                'maximum': 5
            },
            'created_at': {
                'bsonType': 'date'
            },
            'updated_at': {
                'bsonType': 'date'
            }
        }
    }
}

# Создание коллекции refUserRate
ref_user_rate = db.create_collection('refUserRate', validator=ref_user_rate_validator)

# Создание индекса по полю user_id
ref_user_rate.create_index([('user_id', 1)])
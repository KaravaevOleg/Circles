from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['Circles']

teams_validator = {
    '$jsonSchema': {
        'bsonType': 'object',
        'required': ['name', 'description', 'created_by', 'created_at', 'updated_at'],
        'properties': {
            '_id': {
                'bsonType': 'objectId'
            },
            'name': {
                'bsonType': 'string'
            },
            'description': {
                'bsonType': 'string'
            },
            'created_by': {
                'bsonType': 'objectId'
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

teams = db.create_collection('teams', validator=teams_validator)
teams.create_index([('name', 1)], unique=True)

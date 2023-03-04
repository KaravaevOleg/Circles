import pymongo
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

users_validator = {
    '$jsonSchema': {
        'bsonType': 'object',
        'required': ['name', 'surname', 'email', 'password', 'created_at', 'updated_at'],
        'properties': {
            '_id': {
                'bsonType': 'objectId'
            },
            'name': {
                'bsonType': 'string'
            },
            'surname': {
                'bsonType': 'string'
            },
            'email': {
                'bsonType': 'string',
                'pattern': '^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$'
            },
            'password': {
                'bsonType': 'string'
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

ref_user_teams_validator = {
    '$jsonSchema': {
        'bsonType': 'object',
        'required': ['user_id', 'team_id', 'role', 'created_at', 'updated_at'],
        'properties': {
            '_id': {
                'bsonType': 'objectId'
            },
            'user_id': {
                'bsonType': 'objectId'
            },
            'team_id': {
                'bsonType': 'objectId'
            },
            'role': {
                'bsonType': 'string'
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
                'bsonType': 'number'
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

ref_team_rate_validator = {
    '$jsonSchema': {
        'bsonType': 'object',
        'required': ['team_id', 'rated_user_id', 'rating', 'created_at', 'updated_at'],
        'properties': {
            '_id': {
                'bsonType': 'objectId'
            },
            'team_id': {
                'bsonType': 'objectId'
            },
            'rated_user_id': {
                'bsonType': 'objectId'
            }
        }
    }
}
db.refTeamRate.create_index([('team_id', pymongo.ASCENDING), ('rated_user_id', pymongo.ASCENDING)], unique=True)
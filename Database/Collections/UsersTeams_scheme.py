from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['Circles']

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

ref_user_teams = db.create_collection('refUserTeams', validator=ref_user_teams_validator)

ref_user_teams.create_index([('user_id', 1), ('team_id', 1)], unique=True)

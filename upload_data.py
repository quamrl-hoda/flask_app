from pymongo import MongoClient
import pandas as pd
import json

URI = "mongodb+srv://quamrulh987:hoda123@cluster0.8buae.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


# create a new client and connect to server
client = MongoClient(URI)

DATABASE_NAME = "flask_app"

COLLECTION_NAME = "flask_practice"

# import pandas as pd

# Create a simple dataset
data = {
    'id': ['1', '2', '3', '4', '5'],
    'sex': ['male', 'female', 'female', 'male', 'male'],
    'age': [18, 23, 20, 22, 21],
    'federal_district': ['north caucasian', 'volga', 'volga', 'southern', 'southern'],
    'type_of_city': ['village', 'city with population of less than 50k', 
                     'city with population of 1 million and higher', 
                     'city with population of 1 million and higher',
                     'city with population of less than 50k'],
    'knows_election_date': ['named correct date', 'named correct date', 
                            'not sure or no answer', 'named correct date', 
                            'named correct date'],
    'will_vote': ['not sure', 'definitely yes', 'definitely yes', 
                  'definitely yes', 'definitely yes'],
    'candidate': ['Putin', 'Putin', 'Davankov', 'Putin', 'Putin'],
    'television_usage': ['several times a week', 
                         'once half a year',
                         'several times a week',
                         'does not watch',
                         'does not watch'],
    'internet_usage': ['over 4 hours a day'] * 5,
    'education': ['incomplete school education', 
                  'college',
                  'college',
                  'bachelor degree',
                  'bachelor degree'],
    'income': ['very high'] * 5,
    'employment': ['entrepreneur', 
                   'work for hire',
                   'work for hire',
                   'employed student',
                   'unemployed'],
    # Additional columns can be added as needed
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

json_record = list(json.loads(df.T.to_json()).values())

# uploading json data to mongoDB
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

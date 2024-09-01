import pandas as pd
from pymongo import MongoClient
import config

# Function to read CSV file and insert data into MongoDB
def csv_to_mongodb(csv_file, collection_name):
    # Read CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)
    df['ISBN'] = df['ISBN'].astype(str)
    # Connect to MongoDB
    client = MongoClient(config.mongodb_host)
    db = client[config.mongodb_database_name]
    collection = db[collection_name]
    
    # Convert DataFrame to dictionary and insert into MongoDB
    records = df.to_dict(orient='records')
    collection.insert_many(records)
    
    print("Data inserted into MongoDB successfully.")

if __name__ == "__main__":
    csv_file = config.csv_to_mongodb
    collection_name = config.mongodb_collection_name
    csv_to_mongodb(csv_file, collection_name)
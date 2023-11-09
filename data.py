
import json
import pandas as pd
from sqlalchemy import create_engine


def data_preprocessing():
    with open('jobs.json', 'r') as infile:
        json_data = json.load(infile)

    df = pd.json_normalize(json_data)
    df['Job Title'] = df['Job Title'].str.replace('cdi', '', case=False).str.strip()

   
    df = df.rename(columns={
        'Job Title': 'title',
        'Job Location': 'location',
        'Company Name': 'company_name',
        'Job Type': 'job_type'
    })

    return df  

def database_insertion(df):

    database_url = 'postgresql://enesbarut:barut_admin@localhost:5432/jobscraping'

    engine = create_engine(database_url)

    try:
        df.to_sql('job_listings', engine, if_exists='append', index=False)
        print("Data inserted successfully.")
    except Exception as e:
        print("An error occurred: ", e)
        
if __name__ == '__main__':
    df = data_preprocessing()
    database_insertion(df)


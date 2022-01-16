import json
import os.path
import pandas as pd

def load_dataframe():
    file_path=os.path.join(".","data","daily_summaries","daily_summaries_FIPS10003_jan_2018_0.json")
    with open(file_path) as f:
        data=json.load(f)
    
    df_0 = pd.DataFrame(data["results"])

    file_path=os.path.join(".","data","daily_summaries","daily_summaries_FIPS10003_jan_2018_1.json")
    with open(file_path) as f:
        data=json.load(f)
    
    df_1 = pd.DataFrame(data["results"])

    return pd.concat([df_0,df_1])

if __name__ == '__main__':
    print(load_dataframe())
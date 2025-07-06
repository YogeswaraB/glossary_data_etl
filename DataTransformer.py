import pandas as pd
from pandas import json_normalize


class DataTransformer:
    
    def __init__(self, data):
        self.data = data
        
    
    def clean_and_transform(self, raw_data, expected_schema=None):
        #cleansing data
        #convert into pandas
        pd.set_option('display.max_rows', None)      # show all rows
        pd.set_option('display.width', None) 


        pandas_dataframe = pd.DataFrame(raw_data)
        new_df = json_normalize(pandas_dataframe['glossary'])
        new_df['tags'] = new_df['tags'].astype(str)
        new_df['categories'] = new_df['categories'].astype(str)
        # print(new_df.head())
        #remove duplicates
        duplicates = new_df.duplicated().sum()
        if duplicates >= 1:
            print("Yes! there are duplicate rows")
            new_df.drop_duplicates()
        else:
            print("No! there is no dulicate rows")
        #neccessary columns
        new_df.drop(columns = ['layout'])
        return new_df
        
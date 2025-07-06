import requests
from APIClient import APIClient
import pandas as pd
from DataTransformer import DataTransformer
import mysql.connector as mysql
from MySQLHandler import MySQLHandler
from CLIManager import CLIManager


def main():
    base_url = 'https://www.healthcare.gov'
    endpoint = '/api/glossary.json'
    object = APIClient(base_url)
    response = object.fetch_data(endpoint)
    # print(response)

    # pandas_dataframe = yogi.DataFrame(response)
    object_data = DataTransformer(response)
    transformed_data = object_data.clean_and_transform(response)
    

    host = "localhost"
    port = 3306
    user = "root"
    password = "Yogesh@1234"
    database = "sqlpractice"
    connection_object = MySQLHandler(host, port, user, password, database)
    table = connection_object.create_tables()
    table_name = 'glossary_data'
    # data = connection_object.insert_data(table_name, transformed_data)
    sql_query = "SELECT * FROM glossary_data WHERE content LIKE '%plan%'"
    plan_data = connection_object.query_data(sql_query)
    # print(plan_data)
    
    api_client = "test_client"
    # db_handler = "test_handler"
    cli_object = CLIManager(api_client, connection_object)
    cli_object.run()
    close_query = connection_object.close()
   

   

 
   
if __name__ == "__main__":
 main()
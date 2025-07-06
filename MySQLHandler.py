import mysql.connector as mysql
class MySQLHandler:
    
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

        self.connection = mysql.connect(
            host = host,
            port = port,
            user = user,
            password = password,
            database = database)
        self.cur = self.connection.cursor()
        
    def create_tables(self):
        table = self.cur.execute("""
            CREATE TABLE IF NOT EXISTS glossary_data (
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                date TEXT,
                url TEXT,
                content TEXT,
                tags TEXT,
                title TEXT,
                categories TEXT,
                lang TEXT,
                layout TEXT       
            )
            """)
        return table
         
    def insert_data(self, table_name, data_list):
        for i, row in data_list.iterrows():
            self.cur.execute(
                "INSERT INTO glossary_data(date, url, content, tags, title, categories, lang, layout) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (row['date'], row['url'], row['content'], row['tags'], row['title'], row['categories'], row['lang'], row['layout']))
        self.connection.commit()
        
    
    def query_data(self, sql_query, params=None):
        self.cur.execute(sql_query)
        data = self.cur.fetchall()
        return data

       

    def close(self):
        
        self.connection.close() 
import argparse

class CLIManager:
    def __init__(self, api_client, db_handler):
        self.api_client = api_client
        self.db_handler = db_handler
        self.parser = argparse.ArgumentParser(description="Global Healthcare Data ETL & Analysis CLI")
        self._setup_parser()
        
    def _setup_parser(self):
        subparsers = self.parser.add_subparsers(dest='command', help='Available commands')
    
        # # ETL Command
        fetch_parser = subparsers.add_parser('fetch_data', help='Fetch, transform, and load healthcare data.')
        fetch_parser.add_argument('--title', type=str, help='title containing a word. Example plan', required=True)
        # fetch_parser.add_argument('--start_date', type=str, help='Start date (YYYY-MM-DD)')
        # fetch_parser.add_argument('--end_date', type=str, help='End date (YYYY-MM-DD)')
    
        # Query Commands
        query_parser = subparsers.add_parser('query_data', help='Query loaded data.')
        # query_subparsers = query_parser.add_subparsers(dest='query_type', help='Types of queries')
        # top_n_parser = query_subparsers.add_parser('top_n_records', help='Get top N records from table.')
        # top_n_parser.add_argument('number', type=int, help='Number of top records.')
        query_parser.add_argument('--number', type=int, help='number of records.', required=True)
        
        
        # DB Management Commands
        subparsers.add_parser('list_tables', help='List tables in the database.')
        subparsers.add_parser('drop_tables', help='Drop all created tables (USE WITH CAUTION).')
    
    def run(self):
        args = self.parser.parse_args()
        if args.command == 'fetch_data':
            # Logic to call API, transform, and load
            print("fetch_data command")
            sql_query = 'SELECT * FROM glossary_data WHERE title like "' + args.title +'";'
            print(self.db_handler.query_data(sql_query))
            
            pass
    
        elif args.command == 'query_data':
            # Logic to execute SQL queries based on query_type 
            sql_query = 'SELECT * FROM glossary_data LIMIT ' + str(args.number) + ';'
            print(self.db_handler.query_data(sql_query))
            pass
            
        elif args.command == 'list_tables':
            # Logic to list tables
            sql_query = 'SHOW TABLES;'
            print(self.db_handler.query_data(sql_query))
            
            pass
            
        elif args.command == 'drop_tables':
            # Logic to drop tables
            sql_query = 'DROP TABLE glossary_data'
            print(self.db_handler.query_data(sql_query))
            pass
            
        else:
            self.parser.print_help()
            print("help")
import requests

class APIClient:
    def __init__(self, base_url, api_key=None):
        self.base_url = base_url
        self.api_key = api_key
   
    
   
    def fetch_data(self, endpoint, params=None):
        response = requests.get(self.base_url+endpoint).json()
        return response
        
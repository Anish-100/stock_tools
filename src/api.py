import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')

def test():
    r = requests.get('https://api.github.com/events')

class COMMODITY:
    def __init__(self):
        user_data = ''
        wheat_chart = ''
    def get_wheat(self):
        user_data = {'function':'wheat','interval':'annual','datatype':'json','apikey' : api_key}
        temp_wheat = requests.get('https://www.alphavantage.co/query?function=WHEAT',params=user_data)
        return temp_wheat.json()

        

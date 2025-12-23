import requests
import os
import json
from dotenv import load_dotenv
from pathlib import Path

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

class STOCK:
    def __init__(self):
        self.stock_info = ''
        self.symbol = ''
        self.base_path = Path('./src/data')
    
    def get_data(self,symbol:str):
        self.symbol = symbol
        stock_data = None

        if self.check_if_exists() == False:
            stock_data = self.get_api_data()
            with open(f'{self.base_path}/{symbol}.txt','w') as json_file:
                json.dump(stock_data, json_file, indent=4)
        else:
            stock_data = self.get_file_data()

        return stock_data

        

    
    def get_file_data(self):
        '''Gets the data from a local file instead'''
        with open (f'{self.base_path}/{self.symbol}.txt', 'r') as file:
            return json.load(file)
                    
    def get_api_data(self):
        print("API USED!!!")
        symbol = self.symbol
        user_data = {'function':'TIME_SERIES_MONTHLY_ADJUSTED','symbol':symbol,'datatype':'json','apikey' : api_key}
        stock_data = requests.get('https://www.alphavantage.co/query',params=user_data)
        print(stock_data.json())
        return stock_data.json()
    

    def check_if_exists(self):
        for file in self.base_path.iterdir():
            print('FILE',file)
            file = Path(file)
            if not file.is_file():
                pass
            else:
                if file.stem == self.symbol:
                    return True
                else:
                    return False
        return False


        



        

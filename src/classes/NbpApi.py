from typing import Dict
import urllib3
import json
class NbpApi():
    def __init__(self, url: str, format):
        self.url = url
        self.format = format
        self._table = None

    @property
    def table(self):
        return self._table
    
    @table.setter
    def table(self, table):
        self._table = table
    
        
    def get_response_table(self): 
        http = urllib3.PoolManager()
        res = http.request('GET', f"{self.url}/{self.table}?format={self.format}")
        return res
    def get_data_table(self):
        res = self.get_response_table()
        return json.loads(res.data.decode('utf-8'))
        
    def get_table(self, table_name: str):
        self.table = table_name
        data = None
        try:
            data = self.get_data_table()
        except(json.JSONDecodeError) as e:
            raise e
        return data

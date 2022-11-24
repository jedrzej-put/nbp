from typing import Tuple
from .dataclasses.Exchangerates import *
import csv
from datetime import datetime
class CombineData():
    def __init__(self, *args):
        self.data: Tuple(Exchangerates) = args
    
    @staticmethod
    def extract_data(table: Exchangerates):
        for exchangerates in table.data:
            effectiveDate = exchangerates.effectiveDate
            for rate in exchangerates.rates:
                yield [effectiveDate, *rate.dict().values()]
    @staticmethod
    def file_name_generator():
        now = datetime.now()
        return f"out/{now.strftime('%Y-%m-%d--%H-%M-%S')}"
    
    def store_data(self, file_name):
        with open(file_name, 'w', newline='',encoding='utf-8') as csvfile:
            data_writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
            data_writer.writerow(['effectiveDate', 'currency', 'code', 'mid'])
            for table in self.data:
                for row in self.extract_data(table):
                    data_writer.writerow(row)

    def __call__(self) -> None:
        self.store_data(file_name=self.file_name_generator())
    
    
            
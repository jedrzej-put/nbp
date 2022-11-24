from classes.NbpApi import NbpApi 
from classes.CombineData import CombineData
from classes.dataclasses.Exchangerates import Exchangerates
if __name__ == '__main__':
    nbp_api = NbpApi(url="http://api.nbp.pl/api/exchangerates/tables", format="json")
    a = nbp_api.get_table(table_name="a")
    b = nbp_api.get_table(table_name="b")
    combine_data = CombineData(Exchangerates.from_data(a), Exchangerates.from_data(b))
    combine_data()


import pytest, logging, csv, re
from src.classes.CombineData import CombineData
from src.classes.NbpApi import NbpApi
from src.classes.dataclasses.Exchangerates import Exchangerates

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

a=[{'table': 'A', 'no': '227/A/NBP/2022', 'effectiveDate': '2022-11-24', 'rates': [{'currency': 'bat (Tajlandia)', 'code': 'THB', 'mid': 0.1261}, {'currency': 'dolar amerykański', 'code': 'USD', 'mid': 4.5101}]}]
b=[{'table': 'B', 'no': '227/A/NBP/2022', 'effectiveDate': '2022-11-24', 'rates': [{'currency': 'bat (Tajlandia)', 'code': 'THB', 'mid': 0.1261}, {'currency': 'dolar amerykański', 'code': 'USD', 'mid': 4.5101}]}]

@pytest.fixture
def exchangerates_data():
    return Exchangerates.from_data(a)

@pytest.fixture
def combine_data():
    return CombineData(Exchangerates.from_data(a), Exchangerates.from_data(b))


def test_extract_data(exchangerates_data, combine_data):
    gen = combine_data.extract_data(exchangerates_data)
    assert next(gen) == ['2022-11-24', 'bat (Tajlandia)', 'THB', 0.1261]
    assert next(gen) == ['2022-11-24', 'dolar amerykański', 'USD', 4.5101]

def test_store_data(combine_data):
    combine_data.store_data('xd.csv')
    with open('xd.csv', newline='',encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        assert ','.join(next(reader)) == 'effectiveDate,currency,code,mid'
        assert ','.join(next(reader)) == '2022-11-24,bat (Tajlandia),THB,0.1261'
        assert ','.join(next(reader))== '2022-11-24,dolar amerykański,USD,4.5101'
        assert ','.join(next(reader)) == '2022-11-24,bat (Tajlandia),THB,0.1261'
        assert ','.join(next(reader)) == '2022-11-24,dolar amerykański,USD,4.5101'

def test_file_name_generator(combine_data):
    LOGGER.info(re.match("^2022-11-24--23-", combine_data.file_name_generator()))
    assert re.match("^2022-11-24--23-", combine_data.file_name_generator())
    
    
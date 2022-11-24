import pytest
from src.classes.NbpApi import NbpApi
import json
@pytest.fixture
def nbp_api():
    return NbpApi(url="http://api.nbp.pl/api/exchangerates/tables", format="json")

@pytest.fixture
def nbp_api_bad_request():
    return NbpApi(url="http://api.nbp.pl/api/exchangerates/tabless", format="json")

def test_nbp_api_url(nbp_api):
    nbp_api.table = "a"
    assert nbp_api.get_response_table().geturl() == "http://api.nbp.pl/api/exchangerates/tables/a?format=json"

def test_bad_request_url(nbp_api_bad_request):
    nbp_api.table = "a"
    with pytest.raises(json.JSONDecodeError) as exc_info:
        nbp_api_bad_request.get_data_table()
    
    
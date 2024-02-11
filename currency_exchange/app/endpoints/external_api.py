import datetime
import requests
from endpoints.models import GetCurrency,ConvertCurrency
from config import APIKEY
from utils.exceptions import ConvertCurrencyException

class Currency:
    @classmethod
    def get_currency(cls,data: GetCurrency):
        url = f'''https://api.apilayer.com/currency_data/change?start_date={data.start_date}&end_date={data.end_date}&
        &currencies={data.currency}&source={data.source}'''
        payload = {}
        headers= {
          "apikey": APIKEY
        }
        response = requests.request("GET", url, headers=headers, data = payload)
        status_code = response.status_code
        result = response.json()
        if result['success']:
            return {'status_code': status_code, 'result': result}
        if not result['success']:
            raise ConvertCurrencyException(result['error']['info'],result['error']['code'])

    @classmethod
    def convert_currency(cls,data: ConvertCurrency):
        url = f"https://api.apilayer.com/currency_data/convert?to={data.to}&from={data.from_}&amount={data.amount}"

        payload = {}
        headers = {
            "apikey": "hpPa5tZ2B5Ewh1Rh4X6fHYNpcouxgjs7"
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        status_code = response.status_code
        result = response.json()
        if result['success']:
            return {'status_code':status_code,
                    'result':result['result']}
        if not result['success']:
            raise ConvertCurrencyException(result['error']['info'],result['error']['code'])

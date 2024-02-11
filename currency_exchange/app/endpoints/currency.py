from fastapi import APIRouter, Depends
from auth.users import current_active_user
from endpoints.models import GetCurrency,ConvertCurrency
from endpoints.external_api import Currency

router = APIRouter(prefix='/currency')

@router.post('/list',dependencies=[Depends(current_active_user)])
def get_currency_list(data: GetCurrency):
    response = Currency.get_currency(data)
    return response

@router.post('/convert',dependencies=[Depends(current_active_user)])
def convert_currency(data:ConvertCurrency):
    response = Currency.convert_currency(data)
    return response


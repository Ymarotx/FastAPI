from fastapi import HTTPException
from fastapi.responses import JSONResponse
from typing import Any

from starlette import status

custom_message: dict[str,str] = {
    'start_date':'The date should be in the format "yyyy-mm-dd"',
    'end_date':'The date should be in the format "yyyy-mm-dd"',
    'currency':'The currency should be a string',
    'source': 'The currency should be a string',
    'to' : 'The currency should be a string',
    'from_' : 'The currency should be a string',
    'amount' : 'The amount should be integer and greater equal than 0',
}


class ConvertCurrencyException(HTTPException):
    def __init__(self,detail: str, status_code: int) -> None:
        super().__init__(status_code=status_code,detail=detail)



def ValidationError(request,exc):
    errors = []
    for error in exc.errors():
        field = error['loc'][-1]
        msg = custom_message.get(field)
        errors.append({'field':field,'msg':msg,'value':error['input']})
    return JSONResponse(status_code=400,content=errors)
import datetime
from typing import Optional, List, Annotated

from pydantic import BaseModel, Field


class GetCurrency(BaseModel):
    start_date: Optional[str] = datetime.date.today()
    end_date: Optional[str] = datetime.date.today()
    currency: str = 'BYN'
    source: Optional[str] = 'USD'

class ConvertCurrency(BaseModel):
    to: str = 'USD'
    from_: str = 'BYN'
    amount: Annotated[int,Field(ge=0)] = 1

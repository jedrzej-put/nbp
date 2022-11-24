from __future__ import annotations

from typing import List

from pydantic import BaseModel


class Rate(BaseModel):
    currency: str
    code: str
    mid: float


class ExchangeratesItem(BaseModel):
    table: str
    no: str
    effectiveDate: str
    rates: List[Rate]


class Exchangerates(BaseModel):
    data: List[ExchangeratesItem]

    @classmethod
    def from_data(cls, data: List[ExchangeratesItem]) -> Exchangerates:
        return cls.parse_obj({"data": data})
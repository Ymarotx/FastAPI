# ___________________________________________________________________-
# Отложено на потом, когда более детально изучу pytest
# _______________________________________________________________________

from httpx import AsyncClient

async def test_get_currency_list(ac:AsyncClient):
    response = await ac.post("/currency/list", json={
            "start_date": "2024-02-05",
            "end_date": "2024-02-05",
            "currency": "BYN",
            "source": "USD"
        })

    assert response.status_code == 200


async def test_get_currency_convert(ac:AsyncClient):
    response = await ac.post("/currency/convert", json={

            "to": "USD",
            "from_": "BYN",
            "amount": 1
        })

    assert response.status_code == 200
import requests
import pandas as pd

BASE = "https://api.worldbank.org/v2"

def fetch_indicator(country_code: str, indicator:  str) -> pd.DataFrame:
    #f string: permite variaveis dentro da string que, neste caso recebe nos params da funcao 
    url = f"{BASE}/country/{country_code}/indicator/{indicator}?format=json&per_page=20000"


    #faz um get request ao servidor equivalentre a abrir um url no browser 
    r= requests.get(url, timeout=30)
    #importante em prod verifica o status code http 
    # 200 → OK
    # 404 → not found
    # 500 → server error
    # 403 → forbidden
    r.raise_for_status()
    api_result = r.json()


    rows = []

    for item in api_result[1]:
        year = item["date"]
        value = item["value"]

        rows.append({
            "country_code": country_code,
            "indicator": indicator,
            "year": year,
            "value": value

        })

    df = pd.DataFrame(rows)
    #asc, se fosse desc , ascending=False depois fazemos o rest do index senao ficava 5,4,3,2,1,0...
    df = df.sort_values("year").reset_index(drop=True)

    return df
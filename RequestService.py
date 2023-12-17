import requests

from SecretConstants import service_key
from model.SeasonResponse import SeasonResponse
import xml.etree.ElementTree as ET

def get_24_season_data(year, month):
    base_url = "http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/get24DivisionsInfo"
    year = str(year)
    month = str(month)

    if len(month) == 1:
        month = "0" + month
    else:
        month = month

    params = {
        "ServiceKey": service_key,
        "solYear": str(year),
        "solMonth": str(month),
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.text
    else:
        print(f"error: {response.status_code}")
        print(response.text)


def parse_24_season_data(xml_string):
    root = ET.fromstring(xml_string)
    items = root.iter("item")

    parsed_items = []

    for item in items:
        dateName = item.find("dateName").text
        kst = item.find("kst").text
        locdate = item.find("locdate").text
        parsed_items.append(SeasonResponse(dateName, kst, locdate))

    return parsed_items
import requests

from SecretConstants import service_key
from model.SeasonInfo import SeasonInfo
from model.SeasonResponse import SeasonResponse
import xml.etree.ElementTree as ET


class RequestService:
    base_url = "http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/get24DivisionsInfo"

    def get_24_season_data(self, year):
        year = str(year)

        params = {
            "ServiceKey": service_key,
            "solYear": str(year),
            "numOfRows": "500",
        }

        response = requests.get(self.base_url, params=params)

        if response.status_code == 200:
            return response.text
        else:
            print(f"error: {response.status_code}")
            print(response.text)

    def parse_to_season_info_list(self, xml_string):
        root = ET.fromstring(xml_string)
        items = root.iter("item")

        parsed_items = []

        for item in items:
            dateName = item.find("dateName").text
            kst = item.find("kst").text  # 2142  hhmm
            locdate = item.find("locdate").text  # 20041221  yyyymmdd

            year = locdate[:4]
            month = locdate[4:6]
            day = locdate[6:]
            hour = kst[:2]
            minute = kst[2:]

            parsed_items.append(SeasonInfo(dateName, year, month, day, hour, minute))

        return parsed_items

from db import DBService
from excel.ExcelService import ExcelService
from opendataportal.RequestService import RequestService

db_service = DBService.DBService()
request_service = RequestService()


def read_excel_and_insert_db():
    season_info_list = ExcelService().read_excel()

    for season_info in season_info_list:
        db_service.insert_season(season_info)


def request_and_insert_db(now_year):
    max_year_in_db = db_service.max_year_in_db()

    for year in range(max_year_in_db + 1, now_year + 1):
        response_xml = request_service.get_24_season_data(year)
        season_response_list = request_service.parse_to_season_info_list(response_xml)

        for season_response in season_response_list:
            db_service.insert_season(season_response)


# read_excel_and_insert_db()
request_and_insert_db(2024)
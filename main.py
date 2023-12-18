from excel.ExcelService import ExcelService

# import RequestService
# from db import DBService
#
# request_service = RequestService
#
# response_xml = request_service.get_24_season_data(1900, 1)
# season_response_list = request_service.parse_24_season_data(response_xml)
#
# for season_response in season_response_list:
#     print(season_response)
#     print("--------------------------------------------------")
#
#
# db_service = DBService.DBService()
#
# db_service.insert_season(season_response_list[0])


season_info_list = ExcelService().read_excel()

for season_info in season_info_list:
    print(season_info)

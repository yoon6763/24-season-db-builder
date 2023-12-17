import RequestService

request_service = RequestService

response_xml = request_service.get_24_season_data(2021, 1)
season_response_list = request_service.parse_24_season_data(response_xml)

for season_response in season_response_list:
    print(season_response)
    print("--------------------------------------------------")
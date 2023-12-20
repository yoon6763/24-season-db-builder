from db import DBService
from excel.ExcelService import ExcelService
from model.SeasonInfo import SeasonInfo
from opendataportal.RequestService import RequestService
from datetime import datetime, timedelta

db_service = DBService.DBService()
request_service = RequestService()

season_24 = ['소한', '대한', '입춘', '우수', '경칩', '춘분',
             '청명', '곡우', '입하', '소만', '망종', '하지',
             '소서', '대서', '입추', '처서', '백로', '추분',
             '한로', '상강', '입동', '소설', '대설', '동지']


def read_excel_and_insert_past_db():
    season_info_list = ExcelService().read_excel()

    # 소한, 대한, 입춘, 우수, 경칩, 춘분, 청명, 곡우, 입하, 소만, 망종, 하지, 소서, 대서, 입추, 처서, 백로, 추분, 한로, 상강, 입동, 소설, 대설, 동지
    # time_diff = [0.0 for _ in range(24)]
    # count = [0 for _ in range(24)]
    #
    # for i in range(0, 24 * 10):
    #     dt1 = datetime(int(season_info_list[i].year),
    #                    int(season_info_list[i].month),
    #                    int(season_info_list[i].day),
    #                    int(season_info_list[i].hour),
    #                    int(season_info_list[i].minute),
    #                    0)
    #
    #     dt2 = datetime(int(season_info_list[i + 1].year),
    #                    int(season_info_list[i + 1].month),
    #                    int(season_info_list[i + 1].day),
    #                    int(season_info_list[i + 1].hour),
    #                    int(season_info_list[i + 1].minute),
    #                    0)
    #
    #     time_diff[i % 24] += (dt2 - dt1).total_seconds() / 60
    #     count[i % 24] += 1

    # 1950 ~ 1960 평균
    time_diff = [21203.3, 21260.0, 21358.4, 21496.4, 21661.2, 21846.8, 22036.5, 22221.9, 22385.5, 22519.0, 22609.1,
                 22652.2, 22641.9, 22581.3, 22473.1, 22327.3, 22154.1, 21965.0, 21775.4, 21595.9, 21440.4, 21316.0,
                 21233.2, 21191.4]

    temp_date_time = datetime(1900, 2, 4, 15, 44, 0)

    db_service.insert_season(season_info=SeasonInfo("입춘", temp_date_time.year, temp_date_time.month,
                                                    temp_date_time.day, temp_date_time.hour, temp_date_time.minute))

    season_index = 2

    while True:
        temp_date_time += timedelta(minutes=time_diff[season_index])

        if temp_date_time.year >= 1950:
            break

        print(season_24[season_index], temp_date_time)
        season_index += 1
        season_index %= 24

        db_service.insert_season(
            season_info=SeasonInfo(season_24[season_index], temp_date_time.year, temp_date_time.month,
                                   temp_date_time.day, temp_date_time.hour, temp_date_time.minute))


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


def add_future_season():
    # season_list = db_service.get_all_season()
    #
    # season_count = 0
    #
    # time_diff = [0.0 for _ in range(24)]
    #
    # for i in range(0, len(season_list) - 1):
    #
    #     if int(season_list[i+1].year) < 2013:
    #         continue
    #
    #     dt1 = datetime(int(season_list[i].year),
    #                    int(season_list[i].month),
    #                    int(season_list[i].day),
    #                    int(season_list[i].hour),
    #                    int(season_list[i].minute),
    #                    0)
    #
    #     print(season_list[i + 1])
    #
    #     dt2 = datetime(int(season_list[i + 1].year),
    #                    int(season_list[i + 1].month),
    #                    int(season_list[i + 1].day),
    #                    int(season_list[i + 1].hour),
    #                    int(season_list[i + 1].minute),
    #                    0)
    #
    #     season_count += 1
    #     time_diff[season_count % 24] += (dt2 - dt1).total_seconds() / 60
    #
    # print(season_count / 24)
    # print(time_diff)
    # time_diff = [time_diff[i] / (season_count / 24) for i in range(24)]
    # print(time_diff)
    # print(sum(time_diff) / (24 * 60))

    time_diff = [21239.0, 21197.3, 21202.0, 21255.2, 21350.7, 21486.0,
                 21601.2, 21880.6, 22023.0, 22208.5, 22374.0, 22509.6,
                 22605.2, 22647.9, 22643.3, 22586.2, 22482.0, 22338.1,
                 22167.1, 21978.8, 21789.5, 21608.6, 21451.4, 21324.4]

    temp_date_time = datetime(2024, 12, 21, 18, 21, 0)

    season_index = -1

    while True:
        temp_date_time += timedelta(minutes=time_diff[season_index])
        if temp_date_time.year >= 2100:
            break

        season_index += 1
        season_index %= 24

        db_service.insert_season(
            season_info=SeasonInfo(season_24[season_index], temp_date_time.year, temp_date_time.month,
                                   temp_date_time.day, temp_date_time.hour, temp_date_time.minute))


# read_excel_and_insert_past_db()
# read_excel_and_insert_db()
# request_and_insert_db(2024)
add_future_season()

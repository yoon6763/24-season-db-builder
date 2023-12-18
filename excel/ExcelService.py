import pandas as pd

from model.SeasonInfo import SeasonInfo

season_label = ['소한', '대한', '입춘', '우수', '경칩', '춘분',
                '청명', '곡우', '입하', '소만', '망종', '하지',
                '소서', '대서', '입추', '처서', '백로', '추분',
                '한로', '상강', '입동', '소설', '대설', '동지']


class ExcelService:
    path = 'season24.xlsx'

    def read_excel(self):
        year_list = pd.read_excel(self.path, sheet_name=None)

        season_info_list = []

        for year in year_list:
            print("==================================================")
            print(year)
            df = pd.DataFrame(year_list[year])
            df = df.dropna(axis=0)

            for row in df.iterrows():
                season = row[1].iloc[0].split(" ")[0]
                datetime = row[1].iloc[2].split(" ")

                year = datetime[0][:4]
                month = datetime[1][:len(datetime[1]) - 1]
                day = datetime[2][:len(datetime[2]) - 1]
                hour = datetime[3][:len(datetime[3]) - 1]
                minute = datetime[4][:len(datetime[4]) - 1]

                season_info_list.append(SeasonInfo(season, year, month, day, hour, minute))

        return season_info_list

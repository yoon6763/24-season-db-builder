class SeasonInfo:

    def __init__(self, season, year, month, day, hour, minute):
        self.season = season
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute

    def __str__(self):
        return f"season : {self.season}  year : {self.year}  month : {self.month}  day : {self.day}  hour : {self.hour}  minute : {self.minute}"
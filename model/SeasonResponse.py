class SeasonResponse:

    def __init__(self, dateName, kst, locdate):
        self.dateName = dateName

        self.year = locdate[:4]
        self.month = locdate[4:6]
        self.day = locdate[6:]

        self.hour = kst[:2]
        self.minute = kst[2:]

    def __str__(self):
        return f"name : {self.dateName}\n" \
               f"year : {self.year}\n" \
               f"month : {self.month}\n" \
               f"day : {self.day}\n" \
               f"hour : {self.hour}\n" \
               f"minute : {self.minute}\n"

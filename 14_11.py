class SalonBuity:

    min_price = 40

    def __init__(self, time_open, time_close):
        self.time_open = None
        self.time_close = None

    def manic(self):
        print(f"цена маникюра в салоне:{self.min_price*1.20} р")

    def hairs(self, lentgh_hair):
        if lentgh_hair < 30:
            print(f"цена стрижки:{self.min_price*1.20} р")
        elif 30 <= lentgh_hair <= 50:
            print(f"цена стрижки:{self.min_price * 1.50} р")
        elif lentgh_hair > 50:
            print(f"цена стрижки:{self.min_price * 1.80} р")

    def salon_opening_hours(self, time_now = None):
        if time_now != None:
            if  self.time_open <= time_now <= self.time_close:
                print("Магазин работает")
            else:
                print(f"магазин закрыт, время работы с {self.time_open} до {self.time_close}")
        else:
            print(f"время работы с {self.time_open} до {self.time_close}")


class HousWithSalonBuity(SalonBuity):

    def __init__(self, time_open, time_close):
        super().__init__(time_open, time_close)


sb = HousWithSalonBuity(10,22)
sb.salon_opening_hours(8)
print(sb.min_price)
sb.manic()
sb.hairs(23)
sb.hairs(40)
sb.hairs(100)
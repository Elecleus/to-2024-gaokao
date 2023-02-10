# gaokao at 1717718400

import time

class PeriodForm:
    def __init__(self, second, minute, hour, day):
        self.second = second
        self.minute = minute
        self.hour = hour
        self.day = day

    def trans(self):
        hour = self.day * 24 + self.hour
        minute = hour * 60 + self.minute
        second = minute * 60 + self.second

        return(PeriodSec(second))

    def print(self):
        print(f"There are {self.day} days {self.hour} hours {self.minute} minutes {self.second} seconds before gaokao in 2024.\nEveryday is {100/self.day}% of the last days.")

class PeriodSec:

    def __init__(self, length):
        self.length = length

    def trans(self):
        second = self.length

        last_sec = int(second % 60)
        minute = int((second - last_sec) / 60)

        last_min = int(minute % 60)
        hour = int((minute - last_min) / 60)

        last_hour = int(hour % 24)
        day = int((hour - last_hour) / 24)

        return(PeriodForm(last_sec, last_min, last_hour, day))

class TimeUntil:

    def __init__(self):
        self.last_time = PeriodSec(1717718400 + 3600 - int(time.time())).trans()

    def print(self):
        self.last_time.print()

    def draw(self):
        day = [[0, 31], [0, 30], [0, 31], [0, 31], [0, 28], [0, 31], [0, 30], [0, 31], [0, 30], [0, 31], [0, 31], [0, 30], [0, 31], [0, 30], [0, 31], [0, 31], [0, 29], [0, 31], [0, 30], [0, 31], [0, 6]]
        last_time = self.last_time
        last_day = last_time.day

        is_fullday = ( last_time.hour == 0 and last_time.minute == 0 and last_time.second == 0 )

        if not is_fullday:
            last_day += 1
            
        while ( last_day > 0 ):
            for month in range(0, 21):
                month = 20 - month
                while ( day[month][0] < day[month][1] and last_day > 0 ):
                    day[month][0] += 1
                    last_day -= 1

        for month in range(0, 21):
            if day[month][0] != 0 :
                day[month][0] = day[month][1] -day[month][0]
                while day[month][1] != 0:
                    if day[month][0] > 0:
                        print("-",end="")
                        day[month][0] -= 1
                        day[month][1] -= 1
                    else:
                        print("#",end="")
                        day[month][1] -= 1
                print("")
        
def main():
    a = TimeUntil()
    a.print()
    a.draw()
    time.sleep(20)

main()

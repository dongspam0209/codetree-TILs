n=int(input())
class Weather:
    def __init__(self,date,day,weather):
        self.date=date
        self.day=day
        self.weather=weather
arr=[tuple(input().split())for _ in range(n)]
weather_list=[Weather(date,day,weather) for date,day,weather in arr]

target_idx=0
latest_year,latest_month,latest_day=2100,12,31
for idx,weather in enumerate(weather_list):
    if weather.weather=='Rain':
        year,month,day=map(int,weather.date.split("-"))
        if latest_year>year:
            latest_year=year
            target_idx=idx
print(weather_list[target_idx].date,weather_list[target_idx].day,weather_list[target_idx].weather)
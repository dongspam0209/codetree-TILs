# n=int(input())
# class Weather:
#     def __init__(self,date,day,weather):
#         self.date=date
#         self.day=day
#         self.weather=weather
# arr=[tuple(input().split())for _ in range(n)]
# weather_list=[Weather(date,day,weather) for date,day,weather in arr]

# target_idx=0
# latest_year,latest_month,latest_day=2100,12,31
# for idx,weather in enumerate(weather_list):
#     if weather.weather=='Rain':
#         year,month,day=map(int,weather.date.split("-"))
#         if latest_year>year:
#             latest_year=year
#             latest_month=month
#             latest_day=day
#             target_idx=idx
#         elif latest_year==year:
#             if latest_month>month:
#                 latest_year=year
#                 latest_month=month
#                 latest_day=day
#                 target_idx=idx
#             elif latest_month==month:
#                 if latest_day>day:
#                     latest_year=year
#                     latest_month=month
#                     latest_day=day
#                     target_idx=idx
# print(weather_list[target_idx].date,weather_list[target_idx].day,weather_list[target_idx].weather)
# 변수 선언 및 입력
n = int(input())


# Forecast 정보를 나타내는 클래스 선언
class Forecast:
    def __init__(self, date, day, weather):
        self.date, self.day, self.weather = date, day, weather


ans = Forecast("9999-99-99", "", "")
for _ in range(n):
    date, day, weather = tuple(input().split())

    # Forecast 객체를 만들어 줍니다.
    f = Forecast(date, day, weather)
    if weather == "Rain":
        # 비가 오는 경우 가장 최근인지 확인하고,
        # 가장 최근일 경우 정답을 업데이트합니다.
        if ans.date >= f.date:
            ans = f

# 결과를 출력합니다.
print(ans.date, ans.day, ans.weather)
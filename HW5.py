import requests as rq
import pandas as pd
import datetime as dt

url = 'http://api.weatherapi.com/v1/forecast.json?key=6ef0ae2995604023a0372839252106&q=Berlin&days=7&aqi=no&alerts=no' #Berlin data

response = rq.get(url)
data = response.json()

df = pd.DataFrame([{'datetime': hour['time'], #словник із ключами по параметрам метеоумов та значеннями відповідної години дня
                    'temp': hour['temp_c'],
                    'wind_speed': hour['wind_kph']}
                    
                    for day in data['forecast']['forecastday'] #шукаємо ці значення по потрібним словам із результату файлу JSON
                    for hour in day['hour']])
print(df) 

#порахуємо данні із швидкістю вітру. Фактично наша табличка - це великий ліст із 164 значеннями погодних показників.

#щоб відкинути все після 3-ох днів заюзаємо iloc, який відкине непотрібні дні.

df_for_3_days = df.iloc[:72] # 24 * 3 = 72 hours

max_temp = df_for_3_days['temp'].max()
min_temp = df_for_3_days['temp'].min()
mid_temp = df_for_3_days['temp'].mean()
print(max_temp)
print(min_temp)
print(mid_temp)

# сінс вен ві ноу як порахувати середнє, то порахувати суму годин вище середнього  можна через list comprehension з однією умовою
average_wind_speed = df['wind_speed'].mean()
hours_above_average_speed = (df['wind_speed'] > average_wind_speed).sum()
print(hours_above_average_speed)
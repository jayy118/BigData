from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime

#[CODE 1]
def getWeather(result):
    weather_url = 'https://www.weather.go.kr/weather/observation/currentweather.jsp'
    print(weather_url)
    html = urllib.request.urlopen(weather_url)
    soupWeather = BeautifulSoup(html, 'html.parser')
    tag_tbody = soupWeather.find('tbody')
    for city in tag_tbody.find_all('tr'):
        if len(city) <= 10:
            break
        city_td = city.find_all('td')
        city_sido = city_td[0].string
        city_temp = city_td[5].string
        city_humi = city_td[10].string
        result.append([city_sido]+[city_temp]+[city_humi])
    return
                                                
#[CODE 0]
def main():
    result = []
    print('Weather crawling >>>>>>>>>>>>>>>>>>>>>>>>>>')
    getWeather(result)   #[CODE 1] 호출 
    weather_tbl = pd.DataFrame(result, columns=('시, 도', '온도', '습도'))
    weather_tbl.to_csv('./test.csv', encoding='cp949', mode='w', index=True)
      
if __name__ == '__main__':
    main()
     

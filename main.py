import requests
import pandas as pd


if __name__ == '__main__':
    url = 'https://www.haidilao.com/eportal/store/listObjByPosition?longitude=116.403356&latitude=39.905045&mapType=0&country=CN&language=zh'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    df = pd.DataFrame(response.json()['value'])
    # 逆地理编码
    province_list = []
    city_list = []
    district_list = []
    key = 'cbbb04291883b415e6da4ada04a80eb3'
    api_url = 'https://restapi.amap.com/v3/geocode/regeo?'
    for index, location in enumerate(df[['longitude', 'latitude']].values):
        loc = str(location[0]) + ',' + str(location[1])
        api_res = requests.get(url=api_url, params={'key': key, 'location': loc})
        data = api_res.json()['regeocode']['addressComponent']
        province = data['province']
        city = data['city']
        district = data['district']
        if len(city) == 0:
            city = province
        province_list.append(province)
        city_list.append(city)
        district_list.append(district)
    df['province'] = province_list
    df['city'] = city_list
    df['district'] = district_list

    df.to_excel('海底捞门店.xlsx', index=False,encoding='utf-8')


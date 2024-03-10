import time
import json
import datetime
from datetime import datetime
import requests

now=str(datetime.now())
date=now[0:4]+now[5:7]+now[8:10]
target_time=now[11:13]+'00'

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
key="kj9rVtwid/EpOFekRhn+zyu2KBcIReuxj+pLdZ1NuMyi1Im5XORdmUe9lkxXAAHBNqEhOg18ATJOj4Lqs5MM/A=="
params ={'serviceKey' : key, 
        'pageNo' : '1', 
        'numOfRows' : '1000', 
        'dataType' : 'JSON', 
        'base_date' : date,
        'base_time' : str(int(target_time)-100), 
        'nx' : '55', 
        'ny' : '127' }

def get_info():
    temp=0
    response = requests.get(url, params=params)
    data=json.loads(response.text)
    target_list= data['response']['body']['items']['item']
    
    for item in target_list:
        if item['category'] == 'T1H':
            temp=item['obsrValue']
            return temp

def main():
    while(True):
        current_time=date+(str(int(target_time)-100))
        temp=get_info()
        print(f'Temperature {str(current_time)}: {str(temp)} Cº')
        time.sleep(10)

if __name__=='__main__':
    main()


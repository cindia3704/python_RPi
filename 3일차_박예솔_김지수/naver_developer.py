# 파이썬을 활용한 AI 교육 3일차
# Open API 활용 - 공공데이터포털의 '보건복지부_코로나19 감염_현황' xml 파일 데이터 불러오기
# 박예솔, 김지수

import requests, bs4
import urllib.request
from lxml import html
import pandas as pd
from urllib.parse import urlencode, quote_plus, unquote

url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/' 

# url Parameters
key = 'Urpo5gdEG1HGCJWREGJwXp7%2BW1kS3jK8W8MIYQ2QzUruiVv85vE1QuyUlUccn1BXEpHy%2BDJXzti77MpIxmEzJA%3D%3D'
page = '1'
row = '10'
start_day = '20200310'
end_day = '20200315'

parameters = '?serviceKey=' + key + '&pageNo=' + page + '&numOfRows=' + row + '&startCreateDt=' + start_day + '&endCreateDt=' + end_day + '&' 
open_url = url + 'getCovid19InfStateJson' + parameters

req = urllib.request
response = req.urlopen(open_url)
req.get_method = lambda: 'GET'

response_body = response.read()
result = response_body.decode('utf-8')

# Parsing & Make Matrix
xmlobj = bs4.BeautifulSoup(result, 'lxml-xml')
rows = xmlobj.findAll('item')
columns = rows[0].find_all()

rowList = []
nameList = []
columnList = []

rowsLen = len(rows)
for i in range(0, rowsLen):
    columns = rows[i].find_all()
    
    columnsLen = len(columns)
    for j in range(0, columnsLen):
        if i == 0:
            nameList.append(columns[j].name)
        eachColumn = columns[j].text
        columnList.append(eachColumn)
    rowList.append(columnList)
    columnList = []
    
result = pd.DataFrame(rowList, columns=nameList)
result.head()

print(result)
# 년도, 분기
srhYear = 2018
srhPeriod = 1
menuGubun = 'A',
srhType = 'LOC',
houseType = '1',
datas = {
'menuGubun': menuGubun,
'srhType': 'TOT',
'houseType': houseType,
'srhYear': srhYear,
'srhPeriod': srhPeriod,
'gubunCode': 'LAND',
'sidoCode': ''
}
DongDatas = {
'menuGubun': menuGubun,
'srhType': 'TOT',
'houseType':houseType,
'srhYear': srhYear,
'srhPeriod': srhPeriod,
'gubunCode': 'LAND',
'sidoCode': '',
'gugunCode': ''
}
DanjiDatas = {
'menuGubun': menuGubun,
'srhType': 'TOT',
'houseType': houseType,
'srhYear': srhYear,
'srhPeriod': srhPeriod,
'gubunCode': 'LAND',
'sidoCode': '',
'gugunCode': '',
'dongCode': '',
'chosung':'',
'roadCode':'',
'rentAmtType': '3',
'fromAmt1':''
}
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
'Accept':'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
'Connection':'keep-alive',
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie':'ROUTEID=.HTTP1',
'Host':'rt.molit.go.kr',
'Origin':'http://rt.molit.go.kr',
'Referer': 'http://rt.molit.go.kr/idx/main.do',
'X-Requested-With':'XMLHttpRequest'
}

ListDatas = {
'reqPage': 'IDX',
'menuGubun': menuGubun,
'srhType': srhType,
'houseType': houseType,
'srhYear': srhYear,
'srhPeriod': srhPeriod,
'gubunCode': 'LAND',
'sidoCode': '',
'gugunCode': '',
'dongCode': '',
'chosung':'',
'roadCode':'',
'danjiCode':'',
'rentAmtType':'3',
'fromAmt1':'',
'toAmt1':'',
'fromAmt2':'',
'toAmt2':'',
'fromAmt3':'',
'toAmt3':'',
'areaCode':'',
'jimokCode':'',
'useCode':'',
'useSubCode':'',
'jibun':'',
'typeGbn':'',
}
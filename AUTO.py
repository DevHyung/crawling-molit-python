import requests
from bs4 import BeautifulSoup
import json
import pymysql
#### 전역 변수 설정구간
# DB
DB_HOST = 'localhost'
DB_ID = 'root'
DB_PW = 'autoset'
DB_NAME = 'molit'
conn = pymysql.connect(host=DB_HOST, user=DB_ID,  passwd=DB_PW,db= DB_NAME, charset="utf8")
curs = conn.cursor()
sql_apart = """INSERT INTO molit.apart(SRH_YEAR,SRH_PEROID,SRH_TYPE,HOUSE_TYPE,MENU_GUBUN,SIDO,GUGUN,DONG,BLDG_NM,BORN,DEAL_MM,DEAL_DD,BLDG_AREA,APTNO,BLDG_CD,BUILD_YEAR,SUM_AMT)
VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
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
if __name__ == "__main__":
    # NON_AUTO 버전과 다르게 파일에서 가져옴
    f = open("ParseList.txt").readlines()
    ParseList = []
    for line in f:
        ParseList.append(line.strip())

    for ParseStr in ParseList:
        print(ParseStr , '추출중 ...')
        sido,gugun,dong,danji = ParseStr.split('_')

        html = requests.get('http://rt.molit.go.kr/idx/main.do')
        bs4 = BeautifulSoup(html.text,'lxml')
        sidoOption = bs4.find('select',class_='select_s_search')
        sidoDict = {}
        for sidos in sidoOption.find_all('option')[1:]:
            sidoDict[sidos.get_text()] = sidos['value']
        datas['sidoCode'] = sidoDict[sido]
        DongDatas['sidoCode'] = sidoDict[sido]
        DanjiDatas['sidoCode'] = sidoDict[sido]
        ListDatas['sidoCode'] = sidoDict[sido]

        # 시도에따른 구군 리스트 받아오기 및 입력
        gugunDict = {}
        html = requests.post('http://rt.molit.go.kr/srh/getGugunListAjax.do', data=datas)
        jsonString = json.loads(html.text)
        for jsonlist in jsonString['jsonList']:
            gugunDict[jsonlist['NAME']] = jsonlist['CODE']
        DongDatas['gugunCode'] = gugunDict[gugun]
        DanjiDatas['gugunCode'] = gugunDict[gugun]
        ListDatas['gugunCode'] = gugunDict[gugun]

        # 구군에따른 동리 리스트 받아오기 및 입력
        dongDict = {}
        html = requests.post('http://rt.molit.go.kr/srh/getDongListAjax.do', data=DongDatas)
        Dongjson = json.loads(html.text)
        for jsonlist in Dongjson['jsonList']:
            dongDict[jsonlist['NAME']] = jsonlist['CODE']
        DanjiDatas['dongCode'] = dongDict[dong]
        ListDatas['dongCode'] = dongDict[dong]

        # 동리에 따른 단지 리스트 받아오기 및 입력
        danjiDict = {}
        html = requests.post('http://rt.molit.go.kr/srh/getDanjiComboAjax.do', data=DanjiDatas)
        Danjijson = json.loads(html.text)
        danjiDict['전체'] = ''
        for jsonlist in Danjijson['jsonList']:
            danjiDict[jsonlist['NAME']] = jsonlist['CODE']
        if danji == '0':
            ListDatas['danjiCode'] = ''
        else:
            ListDatas['danjiCode'] = danjiDict[danji]
        # 데이터파싱
        html = requests.post('http://rt.molit.go.kr/srh/getListAjax.do', data=ListDatas, headers=headers)
        jsonlists = json.loads(html.text)
        for j in jsonlists['jsonList']:
            NM = j['BLDG_NM']
            BOBN = j['BOBN']
            for M1 in j['month1List']:
                MM = M1['DEAL_MM']
                DD = M1['DEAL_DD']
                AREA = M1['BLDG_AREA']
                APTNO = M1['APTFNO']
                CD = M1['BLDG_CD']
                YEAR = M1['BUILD_YEAR']
                SUMAMT = M1['SUM_AMT']
                curs.execute(sql_apart, (str(srhYear),str(srhPeriod),srhType,houseType,menuGubun,sido,gugun,dong,NM, BOBN, MM, DD, AREA, APTNO, CD, YEAR, SUMAMT))
                conn.commit()
            for M2 in j['month2List']:
                MM = M2['DEAL_MM']
                DD = M2['DEAL_DD']
                AREA = M2['BLDG_AREA']
                APTNO = M2['APTFNO']
                CD = M2['BLDG_CD']
                YEAR = M2['BUILD_YEAR']
                SUMAMT = M2['SUM_AMT']
                curs.execute(sql_apart, (str(srhYear),str(srhPeriod),srhType,houseType,menuGubun,sido,gugun,dong,NM, BOBN, MM, DD, AREA, APTNO, CD, YEAR, SUMAMT))
                conn.commit()
            for M3 in j['month3List']:
                MM = M3['DEAL_MM']
                DD = M3['DEAL_DD']
                AREA = M3['BLDG_AREA']
                APTNO = M3['APTFNO']
                CD = M3['BLDG_CD']
                YEAR = M3['BUILD_YEAR']
                SUMAMT = M3['SUM_AMT']
                curs.execute(sql_apart, (str(srhYear),str(srhPeriod),srhType,houseType,menuGubun,sido,gugun,dong,NM, BOBN, MM, DD, AREA, APTNO, CD, YEAR, SUMAMT))
                conn.commit()
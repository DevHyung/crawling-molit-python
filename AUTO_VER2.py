import requests
from bs4 import BeautifulSoup
import json
from JSON_DATA import *
from DB_CONFIG import *
#### 전역 변수 설정구간

if __name__ == "__main__":
    # NON_AUTO 버전과 다르게 파일에서 가져옴
    # 서울특별시_강남구_개포동_전체 이런식의 포맷으로 되어있으면 파싱을해서 NON_AUTO버전의 입력을 대체하면됌
    f = open("ParseList_VER2.txt").readlines()
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
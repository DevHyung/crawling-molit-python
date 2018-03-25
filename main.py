import requests
from bs4 import BeautifulSoup
import json
datas = {
'menuGubun': 'A',
'srhType': 'TOT',
'houseType': '1',
'srhYear': '2018',
'srhPeriod': '1',
'gubunCode': 'LAND',
'sidoCode': ''
}
DongDatas = {
'menuGubun': 'A',
'srhType': 'TOT',
'houseType': '1',
'srhYear': '2018',
'srhPeriod': '1',
'gubunCode': 'LAND',
'sidoCode': '',
'gugunCode': ''
}
DanjiDatas = {
'menuGubun': 'A',
'srhType': 'TOT',
'houseType': '1',
'srhYear': '2018',
'srhPeriod': '1',
'gubunCode': 'LAND',
'sidoCode': '',
'gugunCode': '',
'dongCode': '',
'chosung':'',
'roadCode':'',
'rentAmtType': '3',
'fromAmt1':''
}
if __name__ == "__main__":
    print(">>> 프로그램시작")
    print(">>> 시도 리스트 받아오는중....")
    html = requests.get('http://rt.molit.go.kr/idx/main.do')
    bs4 = BeautifulSoup(html.text,'lxml')
    sidoOption = bs4.find('select',class_='select_s_search')
    sidoDict = {}
    print('_'*30)
    for sido in sidoOption.find_all('option')[1:]:
        print(sido.get_text() + ":" + sido['value'])
        sidoDict[sido.get_text()] = sido['value']
    print('_' * 30)
    sido = input(">>> 시,도 입력 :")

    datas['sidoCode'] = sidoDict[sido]
    DongDatas['sidoCode'] = sidoDict[sido]
    DanjiDatas['sidoCode'] = sidoDict[sido]

    print('\n'+sido+' 리스트'+'-'*10)
    gugunDict = {}
    html = requests.post('http://rt.molit.go.kr/srh/getGugunListAjax.do', data=datas)
    jsonString = json.loads(html.text)
    for jsonlist in jsonString['jsonList']:
        print('\t' + jsonlist['NAME'] + ":" + jsonlist['CODE'])
        gugunDict[jsonlist['NAME']] = jsonlist['CODE']
    print(sido + ' 리스트' + '-' * 10)
    gugun = input(">>> 구,군 입력 :")

    DongDatas['gugunCode'] = gugunDict[gugun]
    DanjiDatas['gugunCode'] = gugunDict[gugun]

    print('\n' + gugun + ' 리스트' + '-' * 10)
    dongDict = {}
    html = requests.post('http://rt.molit.go.kr/srh/getDongListAjax.do', data=DongDatas)
    Dongjson = json.loads(html.text)
    for jsonlist in Dongjson['jsonList']:
        print('\t\t>>>' + jsonlist['NAME'] + ":" + jsonlist['CODE'])
        dongDict[jsonlist['NAME']] = jsonlist['CODE']
    print(gugun + ' 리스트' + '-' * 10)
    dong = input('>>> 동,리 입력 :')
    DanjiDatas['dongCode'] = dongDict[dong]

    print('\n' + dong + ' 리스트' + '-' * 10)
    danjiDict = {}
    html = requests.post('http://rt.molit.go.kr/srh/getDanjiComboAjax.do', data=DanjiDatas)
    Danjijson = json.loads(html.text)
    print('\t\t\t>>> 전체:0')
    for jsonlist in Danjijson['jsonList']:
        print('\t\t\t>>>' + jsonlist['NAME']+":"+str(jsonlist['CODE']))
    print(dong + ' 리스트' + '-' * 10)

    danji = input('>>> 단지코드 입력 :')

    """
    for sido in sidoOption.find_all('option')[1:]:
        # 시:코드 가지고 구/군을 구함
        print(">>>"+sido.get_text()+":"+sido['value'])
        datas['sidoCode'] = sido['value']
        html = requests.post('http://rt.molit.go.kr/srh/getGugunListAjax.do',data=datas)
        jsonString = json.loads(html.text)
        for jsonlist in jsonString['jsonList']:
            print('\t>>>'+jsonlist['NAME']+":"+jsonlist['CODE'])
            DongDatas['gugunCode'] = jsonlist['CODE']
            html = requests.post('http://rt.molit.go.kr/srh/getDongListAjax.do', data=DongDatas)
            Dongjson = json.loads(html.text)
            for jsonlist in Dongjson['jsonList']:
                print('\t\t>>>' + jsonlist['NAME'] + ":" + jsonlist['CODE'])
            break
        break
        # 구군:코드 를 가지고 읍면동코드를 구함
    """
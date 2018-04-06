import pymysql
DB_HOST = 'localhost'
DB_ID = 'root'
DB_PW = 'autoset'
DB_NAME = 'molit'
conn = pymysql.connect(host=DB_HOST, user=DB_ID,  passwd=DB_PW,db= DB_NAME, charset="utf8")
curs = conn.cursor()
sql_apart = """INSERT INTO molit.apart(SRH_YEAR,SRH_PEROID,SRH_TYPE,HOUSE_TYPE,MENU_GUBUN,SIDO,GUGUN,DONG,BLDG_NM,BORN,DEAL_MM,DEAL_DD,BLDG_AREA,APTNO,BLDG_CD,BUILD_YEAR,SUM_AMT)
VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
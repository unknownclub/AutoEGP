from re import X
from urllib.request import urlopen
import xml.etree.ElementTree as ET
import pandas as pd
from datetime import date
import os


url = 'http://process3.gprocurement.go.th/EPROCRssFeedWeb/egpannouncerss.xml'
parameter_deptId = '?deptId='
parameter_anounceType = '&anounceType='


deptId_txt = open('deptid.txt', 'r')
anounceType_txt = open('anouncetype.txt', 'r')

deptId_ = []
anounceType_ = []

for deptId in deptId_txt:
    deptId_.append(deptId)
for anounceType in anounceType_txt:
    anounceType_.append(anounceType)


today = date.today().strftime('%d%m%Y')
tomonth = date.today().strftime('%B')
toyear = date.today().strftime('%Y')

path_location = 'EGP/' + toyear+ '/' + tomonth

file_csv = path_location + '/' + today + '.csv'

def auto_egp():

    if os.path.isdir(path_location) == False:
        os.makedirs(path_location)

    list_test = {}

    for deptId in deptId_:
        for anounceType in anounceType_:
            url_str = url + parameter_deptId + deptId + parameter_anounceType + anounceType
            url_str = url_str.replace('\n', '')

            url_open = urlopen(url_str)

            root = ET.parse(url_open).getroot()

            # get title
            for rss in root:
                for channel in rss:
                    if channel.tag == 'item':
                        # print(channel.tag)
                        for item in channel:
                            if item.tag == 'description' or item.tag == 'guid':
                                pass
                            else:
                                list_test.update({
                                    item.tag: []
                                })
                        list_test.update({
                            'deptId': []
                        })

            # get data
            for rss in root:
                for channel in rss:
                    if channel.tag == 'item':
                        # print(channel.tag)
                        for item in channel:
                            # print(item.tag)
                            if item.tag == 'description' or item.tag == 'guid':
                                pass
                            else:
                                # print(item.text)
                                list_test[item.tag].append(item.text)
                        deptId_str = deptId
                        deptId_str = deptId_str.replace('\n', '')
                        list_test['deptId'].append(deptId_str)

            # print(list_test)

            df = pd.DataFrame(list_test)

            # .csv ภาษาไทย เอ่อออ

            if os.path.isfile(file_csv) == True:
                df.to_csv(file_csv, index=False, mode='a', header=False)
            else:
                df.to_csv(file_csv, index=False, mode='a')



def data_duplicate():

    # ตัดข้อมูลซ้ำ
    file_csv = path_location + '/' + today + '.csv'
    df = pd.read_csv(file_csv)
    df.drop_duplicates(subset='title', inplace=True)
    # print(df)
    df.to_csv(file_csv, index=False)



def upload():

    df = pd.read_csv(file_csv)
    # print(df)

    from sqlalchemy import create_engine
    engine = create_engine('mysql+pymysql://root:''@localhost:3306/test')
    engine.connect()
    df.to_sql('egp', engine, if_exists='append', index=False)

    # test = engine.execute("SELECT * FROM egp").fetchall()
    # print(test)




print('AUTO E-GP By Avatart0Dev :)')
auto_egp()
data_duplicate()
upload()




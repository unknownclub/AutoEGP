from urllib.request import urlopen
import xml.etree.ElementTree as ET
import pandas as pd
from datetime import date
import os

def pull_egp():
    
    link_txt = open('link.txt', 'r')

    today = date.today().strftime('%d%M%Y')
    tomonth = date.today().strftime('%B')
    toyear = date.today().strftime('%Y')

    path_location = 'EGP/' + tomonth + '/' + toyear

    if os.path.isdir(path_location) == False:
        os.makedirs(path_location)

    list_test = {}

    for _i in link_txt:
        # print(_i)

        url = urlopen(_i)

        root = ET.parse(url).getroot()

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

    # print(list_test)

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

    # print(list_test)

    df = pd.DataFrame(list_test)

    file_csv = path_location + '/' + today + '.txt'     # .csv ภาษาไทย เอ่อออ

    if os.path.isfile(file_csv) == True:
        df.to_csv(file_csv, index=False, mode='a', header=False)
    else:
        df.to_csv(file_csv, index=False, mode='a')



pull_egp()



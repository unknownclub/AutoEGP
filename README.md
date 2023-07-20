# Auto E-GP Python >=3.8

# How to install Packages
    pip install -r requirements.txt

# Database mariadb or mysql


# How to fixed : lookuperror unknown encoding windows-874

Location C:\Users\[username]\AppData\Local\Programs\Python\Python38\Lib\encodings

Edit aliases.py

    # cp874 codec
    '874'                : 'cp874',
    'windows_874'        : 'cp874',


# Add Data

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

import json
import datetime


def load_file(file_name):
    """Достает данные из файла json"""
    with open(file_name, 'r', encoding='utf-8') as file:
        a = json.load(file)
        return a

def created_list (list):
    normal_list=[]
    for i in list:
        if len(i) !=0:
            dic = {}
            dic['date'] = datetime.datetime.strptime(i['date'], '%Y-%m-%dT%H:%M:%S.%f')
            dic['description'] = i['description']
            if dic['description'] == 'Открытие вклада':
                dic['from']=None
            else:
                dic['from'] = i['from']
            dic['to'] = i['to']
            dic['amount'] = i['operationAmount']['amount']
            dic['currency'] = i['operationAmount']['currency']['name']
            dic['state'] = i['state']
            normal_list.append(dic)
    return normal_list


import datetime
import json

def load_file(file_name):
    """Достает данные из файла json в список"""
    with open(file_name, 'r', encoding='utf-8') as file:
        a = json.load(file)
        return a

def created_list (list_):
    """Создает из данных файла массив (список словарей) с нужными полями
     пустые словари и словари с ключом 'stste' отличным от EXECUTED игнорируются
     поле 'data' преобразуется в формат datatime
     отсутсвие поля 'from' ищет по виду операции 'открытие вклада'"""
    normal_list=[]
    for i in list_:
        if len(i) !=0 and i['state'] == "EXECUTED":
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

def output_mask (str_in):
    """Преобразует строку с номером карты/счета в необходимый вид для вывода:
    маска для карты: 'CARD NAME 1234 56** **** 7891
    маска для счета: 'Счет **1234
    в случае отсутсвия значения (поле from) для печати возвращает '' (ничего)"""
    if str_in == None:
        return ''
    else:
        count_int = len ([sym for sym in str_in if sym.isdigit()])
        str_in = str_in.strip()
        str_in = ''.join(reversed(str_in))
        if count_int == 16:
            number = str_in[0:4]+' ****'+' **'+str_in[10:12]+' '+str_in[12:16]
            name = str_in[16:]
        else:
            number = str_in[0:4]+'**'
            name = str_in[20:]
    return ''.join(reversed(name))+''.join(reversed(number))

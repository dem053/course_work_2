import json
import datetime
from functions import load_file, created_list

FILE_NAME = 'operations.json'

list = load_file(FILE_NAME)

normal_list = created_list(list)
normal_list = sorted(normal_list, key=lambda x: x['date'], reverse=True)
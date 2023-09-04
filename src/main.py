from functions import load_file, created_list, output_mask

FILE_NAME = 'operations.json' # путь к фалу с данными


list_ = load_file(FILE_NAME)
normal_list = created_list(list_)
normal_list = sorted(normal_list, key=lambda x: x['date'], reverse=True)
for i in range(5):
    print(f'{normal_list[i]["date"].strftime("%d.%m.%Y")} {normal_list[i]["description"]}')
    print(f'{output_mask(normal_list[i]["from"])} -> {output_mask(normal_list[i]["to"])}')
    print(f'{normal_list[i]["amount"]} {normal_list[i]["currency"]}\n')

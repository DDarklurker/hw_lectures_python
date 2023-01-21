"""
Завантажити з data.json данні та перезаписани їх як вказано в файлах split_format, index_format, column_format
Ускладнений варіант - напишіть ассет до цього завдання самі

"""
import json
"""
FileNotFoundError: [Errno 2] No such file or directory: 'data.json'
При запуску я отримав цю помилку. Будь ласка кладіть всі необхідні для роботи файли сюди.

Більш менш ок. Аее якщо я вам дам json  на 1000 рядків? також руками все будете перебирати? 
"""
with open("data.json", "r") as file:
    data_j = json.load(file)
    file.close()
data_list = data_j["data"]
colum_f = {}
# як би окей що ви робите дел... але ви трошки себе путаєте.
# программа має бути правилом перекладу одного джей сон в інший.
# все ж таки варто пояснити як перекласти(переложить - свинособача) одні данні в іншу структура
# а не як виліпити з однієї структури 2-гу
for i in range(len(data_list)):
    colum_f[data_list[i]['index']] = data_list[i]
    del colum_f[data_list[i]['index']]['index']
with open("index_format.json", "w", encoding="utf-8") as file:
    json.dump(colum_f, file)
with open("data.json", "r") as file:
    data_j = json.load(file)
    file.close()
data_list = data_j["data"]
split_f = {}
value_colum = []
print(data_list)
for attributes in data_list[0].keys():
    value_colum.append(attributes)
    split_f['columns'] = value_colum
split_f['columns'].pop(0)
value_index = []
for i in range(len(data_list)):
    value_index.append(data_list[i]['index'])
    split_f['index'] = value_index
value_data_1 = []
value_data_2 = []
"""
Більш менш ок. Аее якщо я вам дам json  на 1000 рядків? також руками все будете перебирати? Програма має бути не залежною
від розміру вхідних данних!!!! 
"""
value_data_1.append([data_list[0].get('col 1')])
value_data_1.append([data_list[0].get('col 2')])
value_data_2.append([data_list[1].get('col 1')])
value_data_2.append([data_list[1].get('col 2')])
split_f['data'] = value_data_1
split_f['data'] = value_data_2
print(split_f)

with open("split_format.json", "w", encoding="utf-8") as file:
    json.dump(split_f, file)

assert file('index_format.json') == {"row 1": {"col 1": "a", "col 2": "b"}, "row 2": {"col 1": "c", "col 2": "d"}}
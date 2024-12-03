import json

text = {1 : 'Hello file World!'}  # Инфо что добавляется в файл

with open('myfile.txt' , 'w') as f: # Создать файл в этой же директории
    json.dump(text, f)
import json

with open('myfile.txt') as f: # Открыть и прочитать созданный файл
    text = json.load(f)
    print(text)
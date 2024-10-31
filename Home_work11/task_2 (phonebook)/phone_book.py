import json
phonebook_json = {
    "name": "Alice",
    "surname": "Johnson",
    "phone": "123-456-7890",
    "address": "123 Main St. Toronto.Canada",
    "job": "Engineer",
    "info": "Loves hiking"
}

with open('Phone book.json' , 'w') as file: #Добавление нового справочника
    json.dump(phonebook_json , file)

with open('Phone book.json') as file:  # Чтение справочника
    phonebook = json.load(file)
    for key , value in phonebook.items():
        print(f'{key} : {value}')

print('---' * 10)

if phonebook["name"] == 'Alice':   # Поиск по имени
    print('Found a record:', phonebook)
else:
    print('Person not found.')

print('---' * 10)

if phonebook["surname"] == 'Johnson':  #Поиск по фамилии
    print('Found a record:', phonebook)
else:
    print('Person not found.')

print('---' * 10)

if phonebook["phone"] == '123-456-7890':  #Поиск по номеру
    print('Found a record:', phonebook)
else:
    print('Person not found.')

print('---' * 10)

if phonebook ['name'] == 'Alice' and phonebook ['surname'] =='Johnson':  #Обновление записи для данного  номера
    phonebook ['phone'] ='890-888-2024'
    print("The phone number has been changed to:", phonebook["phone"])
else:
    print("Person not found.")

print('---' * 10)

with open('Phone book.json' , 'w') as file: # Cохранение результата
    json.dump(phonebook, file)

with open('Phone book.json') as file:  # Чтение справочника
    phonebook = json.load(file)
    for key , value in phonebook.items():
        print(f'{key} : {value}')









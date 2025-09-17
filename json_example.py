import json

data = {
    "name": "Мария",
    "age": 25,
    "is_student": True
}

json_string = json.dumps(data, indent=4)  # Преобразуем Python-объект в JSON-строку
print(json_string)


with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)  # Загружаем JSON из файла
    print(data)

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)  # Сохраняем JSON в файл
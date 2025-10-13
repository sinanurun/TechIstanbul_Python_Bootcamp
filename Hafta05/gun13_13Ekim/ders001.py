import json

# JSON string'i Python dict'e çevirme
json_string = '{"name": "Ali", "age": 25, "city": "İstanbul"}'
python_dict = json.loads(json_string)
print(python_dict["name"])  # Ali

# Python dict'i JSON string'e çevirme
python_dict = {"name": "Ayşe", "age": 30}
json_string = json.dumps(python_dict, ensure_ascii=False)
print(json_string)  # {"name": "Ayşe", "age": 30}
# string jsn nesne oluşturma

import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
print(type(y["age"]))

class Ogrenci():
    def __init__(self,kwargs):
        self.ad = kwargs["name"]
        self.age = kwargs["age"]
        self.city = kwargs["city"]
og = Ogrenci(y)
# og = Ogrenci(name="ali",age=15,city = "izmir")
print(og.ad)
print(vars(og))


# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
print(type(y))
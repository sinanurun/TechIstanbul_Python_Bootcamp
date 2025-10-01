import json

# Python objesini JSON string'e çevirme
data = {"isim": "Ali", "yas": 30, "sehirler": ["İstanbul", "Ankara"]}
json_str = json.dumps(data, ensure_ascii=False, indent=2)
print(json_str, type(json_str))

# JSON string'ini Python objesine çevirme
parsed = json.loads(json_str)
print(type(parsed))
print(parsed["isim"])  # Ali

# Dosyaya JSON yazma
with open("veri.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# JSON dosyasını okuma
with open("veri.json", "r", encoding="utf-8") as f:
    okunan = json.load(f)
    print(okunan)


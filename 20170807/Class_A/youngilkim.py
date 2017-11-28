import json
a = { "k": [0, {"k2": "hello"}, 2]}
print(a['k'][1]["k2"])

print(json.dumps(a))
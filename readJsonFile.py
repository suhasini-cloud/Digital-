import json

# Reading data back
with open('/Users/SUHAS/PycharmProjects/untitled/data/data.json', 'r') as f:
     data = json.load(f)

print(data)

f.close()
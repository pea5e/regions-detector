import json 

with  open("regions.json" , 'r',encoding="utf-8") as f :
  r = f.read() 

js = json.loads(r)

print(js.keys())

js["objects"]["regions"]["geometries"] 

l = list()
for j in js["objects"]["regions"]["geometries"]:
  if j["type"]=="MultiPolygon" :
    for i in j["arcs"]:
      l.extend(i[0])
  else :
    l.extend(j["arcs"][0])

l = list(map(lambda x:  x*-1-1 if x<0 else x,l))
print(l)
print(len(js["arcs"]))

remove = list()

for i in range(len(js["arcs"])):
  if i not in l:
    remove.append(i)
    print(i)


for i in remove:
  js["arcs"][i] = [[]]

with open("region-v2.json" , 'w',encoding="utf-8") as file:
  file.write(json.dumps(js))


import json 

with  open("regions copy 2.json" , 'r',encoding="utf-8") as f :
  r = f.read() 

js = json.loads(r)

print(js.keys())
transform = js["transform"]
arcs = len(js["arcs"])

# js["objects"]["regions"]["geometries"] 

# l = list()
# for j in js["objects"]["regions"]["geometries"]:
#   if j["type"]=="MultiPolygon" :
#     for i in j["arcs"]:
#       l.extend(i[0])
#   else :
#     l.extend(j["arcs"][0])

# l = list(map(lambda x:  x*-1-1 if x<0 else x,l))

# print(l)

# print(len(js["arcs"]))

# remove = list()

# for i in range(len(js["arcs"])):
#   if i not in l:
#     remove.append(i)
#     print(i)


# for i in remove:
#   js["arcs"][i] = [[]]

# with open("region-v2.json" , 'w',encoding="utf-8") as file:
#   file.write(json.dumps(js))

print(transform)


coord = (35.686015, -5.820450)


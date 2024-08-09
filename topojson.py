from json import loads

with  open("regions.json" , 'r',encoding="utf-8") as f :
  r = f.read() 

js = loads(r)

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
for i in range(len(js["arcs"])):
  if i not in l:
    print(i)

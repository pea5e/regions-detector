from json import loads

with  open("regions.json" , 'r') as f :
  r = f.read() 

js = loads(r)

print(js.keys())

js["objects"]["regions"]["geometries"] 

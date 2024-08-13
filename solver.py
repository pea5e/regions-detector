import json 

with  open("regions copy 2.json" , 'r',encoding="utf-8") as f :
  r = f.read() 

js = json.loads(r)

transform = js["transform"]
arcs = len(js["arcs"])
regions = js["objects"]["regions"]["geometries"] 

coord = (33.466255, -5.786114) #Beni Mellal
coord = (33.470412, -5.784583) #Fes
coord = (33.470167, -5.787494) #Rabat

x = coord[1] - transform["translate"][0];
y = coord[0] - transform["translate"][1];


xperScale = x / transform["scale"][0]
yperScale = y / transform["scale"][1]


l = list()

for region in regions:
    for arcIndex,arc in enumerate(region["arcs"][0]):
        x = arc if arc >= 0 else arc*-1-1
        cpath = [js["arcs"][x][0][0],js["arcs"][x][0][1]]
        for dirIndex,dirs in enumerate(js["arcs"][x][1:],start=1):
            if (cpath[1]<=yperScale and cpath[1]+dirs[1]>=yperScale) or (cpath[1]>=yperScale and cpath[1]+dirs[1]<=yperScale):
                l.append(cpath[0]+abs(abs(yperScale-cpath[1])/dirs[1])*dirs[0])
            cpath[0] = cpath[0]+dirs[0]
            cpath[1] = cpath[1]+dirs[1]
    l = sorted(l)
    for i,e in enumerate(l[::2]):
        if xperScale>=e and xperScale<=l[i*2+1]:
            print(region["properties"]["name"])
            exit()
    l.clear()

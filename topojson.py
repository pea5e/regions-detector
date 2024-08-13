# import json 

# with  open("regions.json" , 'r',encoding="utf-8") as f :
#   r = f.read() 

# js = json.loads(r)

# print(js.keys())

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


import json 

with  open("regions copy 2.json" , 'r',encoding="utf-8") as f :
  r = f.read() 

js = json.loads(r)

print(js.keys())
transform = js["transform"]
arcs = len(js["arcs"])
regions = js["objects"]["regions"]["geometries"] 

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
# print(regions)


# coord = (35.686015, -5.820450)
coord = (34.614845, -5.288887)
coord = (35.549780, -5.574435)
coord = (34.582470, -5.316348)
coord = (34.796643, -5.289176)

x = coord[1] - transform["translate"][0];
y = coord[0] - transform["translate"][1];

print(x,y)

xperScale = x / transform["scale"][0]
yperScale = y / transform["scale"][1]

print(xperScale,yperScale)


# for arcIndex,arc in enumerate(regions[0]["arcs"][0]):
#     x = arc if arc >= 0 else arc*-1-1
#     cpath = [js["arcs"][x][0][0],js["arcs"][x][0][1]]
#     for dirIndex,dirs in enumerate(js["arcs"][x][1:],start=1):
#         if (cpath[1]<=yperScale and cpath[1]+dirs[1]>=yperScale) or (cpath[1]>=yperScale and cpath[1]+dirs[1]<=yperScale):
#             # print(cpath,dirs)
#             for arcs2Index,arc2 in enumerate(regions[0]["arcs"][0][arcIndex:]):
#                 arc2 = arc2 if arc2 >= 0 else arc2*-1-1
#                 if arcs2Index==arcIndex:
#                     cpath2 = [cpath[0],cpath[1]]
#                 else :
#                     cpath2 = [js["arcs"][arc2][0][0],js["arcs"][arc2][0][1]]

#                 for dir2Index,dir2 in enumerate(js["arcs"][x][1+(dirIndex*int(arcs2Index==arcIndex)):],start=1+(dirIndex*int(arcs2Index==arcIndex))):
#                     cpath2[0] = cpath2[0]+dir2[0]
#                     if (cpath2[1]<=yperScale and cpath2[1]+dir2[1]>=yperScale) or (cpath2[1]>=yperScale and cpath2[1]+dir2[1]<=yperScale):
#                         print("cpath2",cpath2[0],cpath[0])
#                         if(cpath2[0]<=xperScale and cpath[0]>=xperScale) or (cpath2[0]>=xperScale and cpath[0]<=xperScale):
#                             print("inside :")
#                             print(cpath2,dir2,arcIndex,arcs2Index,dir2Index,dirIndex)
#                             print(cpath2[0]*transform["scale"][0],cpath[0]*transform["scale"][0])
#                             print(transform["translate"][0]+cpath2[0]*transform["scale"][0],transform["translate"][0]+cpath[0]*transform["scale"][0])
#                             exit()
#                     cpath2[1] = cpath2[1]+dir2[1]
#         cpath[0] = cpath[0]+dirs[0]
#         cpath[1] = cpath[1]+dirs[1]

# l = list()

# for arcIndex,arc in enumerate(regions[0]["arcs"][0]):
#     print(arc)
#     x = arc if arc >= 0 else arc*-1-1
#     cpath = [js["arcs"][x][0][0],js["arcs"][x][0][1]]
#     for dirIndex,dirs in enumerate(js["arcs"][x][1:],start=1):
#         if (cpath[1]<=yperScale and cpath[1]+dirs[1]>=yperScale) or (cpath[1]>=yperScale and cpath[1]+dirs[1]<=yperScale):
#             # print(cpath,dirs)
#             l.append([[cpath[0]+(abs(yperScale-cpath[1])/dirs[1])*dirs[0],yperScale],cpath,arcIndex,dirIndex,dirs,arc])
#         cpath[0] = cpath[0]+dirs[0]
#         cpath[1] = cpath[1]+dirs[1]

# print(l)

l = list()

for arcIndex,arc in enumerate(regions[0]["arcs"][0]):
    x = arc if arc >= 0 else arc*-1-1
    cpath = [js["arcs"][x][0][0],js["arcs"][x][0][1]]
    for dirIndex,dirs in enumerate(js["arcs"][x][1:],start=1):
        if (cpath[1]<=yperScale and cpath[1]+dirs[1]>=yperScale) or (cpath[1]>=yperScale and cpath[1]+dirs[1]<=yperScale):
            l.append([[cpath[0]+(abs(yperScale-cpath[1])/dirs[1])*dirs[0],yperScale],cpath,arcIndex,dirIndex,dirs,arc])
            if len(l)==2:
                print(l)
                if ((l[0][0][0]<=xperScale and l[1][0][0]>=xperScale) or (l[0][0][0]>=xperScale and l[1][0][0]<=xperScale)) and (( l[0][-1]==l[1][-1] and l[1][-1]>=0 ) or l[0][-1]!=l[1][-1]) : 
                    print("included\n")
                    exit()
                l.clear()
        cpath[0] = cpath[0]+dirs[0]
        cpath[1] = cpath[1]+dirs[1]

print(l)

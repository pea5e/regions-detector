import cv2 



region = {
    0: "not in map",
    255: "Border",
    135: "Tanger-Tétouan-Al Hoceïma",
    84: "Oriental",
    160: "Rabat-Salé-Kénitra",
    101: "Fès-Meknès",
    168: "Casablanca-Settat",
    163: "Béni Mellal-Khénifra",
    193: "Drâa-Tafilalet",
    123: "Marrakech-Safi",
    153: "Souss-Massa",
    120: "Guelmim-Oued Noun",
    109: "Laâyoune-Sakia El Hamra",
    148: "Dakhla-Oued Ed-Dahab"
}

img = cv2.imread(r"Map_of_the_regions_of_Morocco v1.png",0)
rows,cols = img.shape
print(rows,cols)
# for i in range(rows):
#     for j in range(cols):
#         k = img[i,j]
#         print(k)
north = (35.91744,-5.4024861)
south = (20.7699868,-17.050552)

west = (20.843596, -17.104512)
east = (32.509632,-0.9954204)
longitude = north[0]-south[0]
latitude = east[1]-west[1]
# print(longitude)
# print(latitude)
yByPix = longitude/rows
xByPix = latitude/cols
# print(yByPix)
# print(xByPix)
coord = (32.731094, -9.043965)
y = north[0]-coord[0]
x = coord[1]-west[1]
print(y//yByPix,x//xByPix)
c = int(img[int(y/yByPix),int(x/xByPix)])
y = y//yByPix
x = x//xByPix
# c = int(img[400,2500])
d = 1
while c==0 or c==255:
    # print()
    c = int(img[int(y+ ((d-1)//4+1)*((d%2)+(d%4>1)*-1)),int(x+ ((d-1)//4+1)*(((d+1)%2)+(d%4>1)*-1))])
    d+=1



print(region[c])



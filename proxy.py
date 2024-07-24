from flask import Flask, jsonify, request, Response
import cv2 
from requests import get,post




app = Flask(__name__)

@app.route("/verify")
def verify():
    verificationCode = request.form['verificationCode']



@app.route("/Region/<lat>,<lon>")
def region(lat,lon):
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

    north = (35.91744,-5.4024861)
    south = (20.7699868,-17.050552)

    west = (20.843596, -17.104512)
    east = (32.509632,-0.9954204)
    longitude = north[0]-south[0]
    latitude = east[1]-west[1]
  
    yByPix = longitude/rows
    xByPix = latitude/cols
    
    coord = (float(lat),float(lon))
    #    print(coord)
    y = north[0]-coord[0]
    x = coord[1]-west[1]

    c = int(img[int(y/yByPix),int(x/xByPix)])
    y = y//yByPix
    x = x//xByPix
    # c = int(img[400,2500])
    d = 1
    while c==0 or c==255:
        c = int(img[int(y+ ((d-1)//4+1)*((d%2)+(d%4>1)*-1)),int(x+ ((d-1)//4+1)*(((d+1)%2)+(d%4>1)*-1))])
        d+=1



    #   print(region[c])

  
    return jsonify({"Region":region[c]})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=["GET", "POST"])
def proxy(path):
    headers = request.headers
    # data = request.json
    data = ""

    print(path,headers,data)
    request(path)
    return "hello ,world!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4400, debug=False)

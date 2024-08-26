from requests import post ,get


# req = post("http://127.0.0.1:8080/api/auth/signup",
#             headers={'Content-type': 'application/json'},
#            json = {
#                "Name":"Salim",
#                "Email":"kngs1023@gmail.com",
#                "Password":"Salim123",
#                "Tel":"0567894590",
#                "Cin":"bg789057"
#                }
#            )

req = post("http://127.0.0.1:8080/api/auth/login",
           headers={'Content-type': 'application/json'},
           json = {
               "Email":"farmer",
               "Password":"farmer"
               }
           )


token = req.content.decode()
# token = 'eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzZWxmIiwic3ViIjoiZmFybWVyIiwiZXhwIjoxNzI0NzU0NzIwLCJpYXQiOjE3MjQ2NjgzMjB9.W9u3avQG3xmRXM5q-cEjnMWo9Os4iDbRO80DYH4wg5E'
print(token)



req = post("http://127.0.0.1:8080/api/farms/add",
           headers= {
               "Authorization":"Bearer "+token,
               'Content-type': 'application/json'
               },
               json={
                   "title" : "farm2",
                   "region" : 0,
                   "province" : 0,
                   "commune" : "tanger",
                   "douar" : "tayga",
                   "coordinates" : {
                       "lat" :35.711421,
                       "lon" :-5.813164
                   }
               }
           )

########################
# req = post("http://127.0.0.1:8080/api/farms/get",
#            headers= {
#                "Authorization":"Bearer "+token
#                }
#            )

# private String title;

#     private int region;
    
#     private int province;

#     private String commune;
    
#     private String douar;

#     private Farmer farmer;
    
#     private Coordinates coordinates;


print(req.content)

coord = [34.026799, -6.811300]
req = post("http://127.0.0.1:8080/api/region/get",
           json={"lon":coord[1],"lat":coord[0]}
           )


print(req.content.decode(encoding="utf-8"))
print(req.status_code)

import requests

link = 'https://httpbin.org/post'
data = {"comments":"Say Hello",
        'custemail':"asdf@gmail.com",
        "custtel":"+998997777777",
        "custname":"Mickel Jordan",
        "delivery":"20:30",
        "size":"large",
        "topping":["mushroom","cheese"]}


print(requests.post(link, data).status_code)
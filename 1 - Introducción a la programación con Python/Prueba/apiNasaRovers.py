import json
import requests


def request(url, api_key):
    headers = {
        'Cache-Control': "no-cache",
        'Postman-Token': "6e40dc6a-88b6-44c6-8f00-e85966591a94,f1432b74-2522-48e1-95d2-731bcc97f8ac",
    }
    url_comp = url+"?sol=1&api_key=" + api_key
    response = requests.request("GET", url_comp, headers=headers)
    return(json.loads(response.text))


def build_web_page(json):
    list_image = []
    for image_data in json["photos"]:
        list_image.append(image_data["img_src"])

    header = "<html>\n<head>\n</head>\n<body>\n<ul>"
    li = ""

    for image_src in list_image:
        li = "\n\t<li><img src='{}'></li>".format(image_src) + li

    footer = "</ul>\n</body>\n</html>"

    html = header + li + footer

    with open("output.html", "w") as f:
        f.write(html)
        f.close()

json = request("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos", "pdf7ivg3mxhFfMhg5fpHFfU78SNpjQdVk5GUPiJr")

build_web_page(json)

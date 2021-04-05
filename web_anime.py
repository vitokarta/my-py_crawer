import urllib.request as request
# import json
web="https://www.instagram.com/"
with request.urlopen(web) as respond:
    data=respond.read().decode("utf-8")
    # data=json.load(respond)
print(data)
# click=data["result"]["results"]
# for company in click:
#     print(company["公司地址"])

# with open("company.txt",mode="w",encoding="utf-8") as file:
#     for company in click:
#         file.write(company["公司名稱"]+'\n')
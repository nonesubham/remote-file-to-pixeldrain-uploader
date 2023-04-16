import requests

url = input("Enter File URL : ")
file_name = input("Enter File Name With Extension : ")
file_source = requests.get(url)
file=file_source.content

response = requests.post(
    "https://pixeldrain.com/api/file",
    
    data={"name":file_name,"anonymous": True},
    files={"file": file}
)
resp=(response.json())
print(f"https://pixeldrain.com/u/{resp['id']}")
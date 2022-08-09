import requests
res=requests.get('http://127.0.0.1:5000/test',{'FirstName':'Haya','LastName':'Adawi','Class':'9','section':'A','ADDRESS':'Amman'})
print(res.text)
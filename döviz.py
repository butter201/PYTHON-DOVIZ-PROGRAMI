import requests
from bs4 import BeautifulSoup
url="https://www.doviz.com/"
response=requests.get(url)
icerik=response.content
soup=BeautifulSoup(icerik,"html.parser")
doviz=soup.find_all("span",{"class":"name"})
deger=soup.find_all("span",{"class":"value"})
for i,j in zip(doviz,deger):
    i=i.text
    j=j.text
    print("Birim ==> {} \nDeger ==> {}".format(i,j))
    print("----------")
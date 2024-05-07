import requests #web siteleriyle iletişim kurmak için kütüphane
from bs4 import BeautifulSoup #sayfadan istediğimiz bileşeni çekmemizi sağlayacak
from mail import sendMail

url1="https://www.trendyol.com/combine-michail/standart-kalip-basic-relaxed-5-li-paket-t-shirt-p-676945562?boutiqueId=61&merchantId=165925" #takip etmek istediğimiz ürünün url i

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
} #sunucunun isteği gerçekleştirmesi için gönderilen isteğin hangi tarayıcı ve sürümü tarafından yapılacağını belirler

page =requests.get(url1, headers=headers) #sorguyu değişkene atadık

htmlpage=BeautifulSoup(page.content,"html.parser") #sayfanın bileşenini html parser kullanarak alıyoruz

producttitle=htmlpage.find("h1", class_="pr-new-br").getText() #ürünün başlığını almalıyız bu yüzden h1 bileşeninde bulunan class ismi pr-new-br olan sınıfı alıyoruz ve başlık değişkenine atıyoruz sonra getText metoduyla sadece metinleri alıyoruz

price=htmlpage.find("span",class_="prc-dsc").getText() #ücretini aynı şekilde bulup değişkene atıyoruz

image=htmlpage.find("img",class_="base-product-image") #görseli değişkene atıyoruz

convertedprice=float(price.replace(",",".").replace("TL","")) #ücreti floata çevirip virgüllü ifadeyi noktaya TL ifadesinide yok ediyoruz


if (convertedprice <= 700):
    print("Ürünün fiyatı düştü")  #ürünün fiyatı 600 veya daha aza düşerse terminale bu metni bastırsın 
    htmlecontent="""\
     <html>
     <head></head>
     <body>
     <h3>{0}</h3>   
     <br/>
     {1}
     <br/>
     <p>Ürün Linki: {2}</p>
     </body>
     </html>
""".format(producttitle,image,url1)
    sendMail("can-1045@hotmail.com","Ürünün fiyatı düştü",htmlecontent,) #ürünün fiyatı düştüyse mail.py de tanımladığımız fonksiyonu çalıştırsın
print(convertedprice)

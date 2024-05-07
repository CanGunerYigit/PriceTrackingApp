import smtplib #mail göndermek için gerekli kütüphane
from email.mime.multipart import MIMEMultipart #mailimizde resim metin video gibi farklı içeriklerin bir araya getirilmesini sağlar
from email.mime.text import MIMEText

def sendMail(toMail,subject,content):   #mail atmak için fonksiyon oluşturduk kime gönderilecek, konusu ve içerik için değişkenler tanımladık
    fromMail="mailiniz" #mail kimden gidecek
    server=smtplib.SMTP("smtp.live.com",587) #hotmail için sunucuya bağladık aynısı gmail içinde yapılabilir 

    server.starttls()

    server.login(fromMail,"şifreniz") #mail hesabına giriş yapmamız gerek 

    message=MIMEMultipart('alternative')
    message['Subject']=subject #konumuz

    htmlcontent= MIMEText(content,'html')

    message.attach(htmlcontent)  #mailimizin içine html içeriği ekliyoruz

    server.sendmail(
        fromMail,
        toMail,
        message.as_string()
    )

    server.quit()
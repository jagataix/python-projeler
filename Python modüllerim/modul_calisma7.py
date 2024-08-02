import smtplib

from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText

import sys

mesajım = MIMEMultipart()

mesajım ["From"] = "musicbyjagatai@gmail.com"

mesajım ["To"] = "musicbyjagatai@gmail.com"

mesajım ["Subject"] = "Mail gönderiyorum"


metin = """

ben buraya birşeyler yazacağım

çok güzel

baya iyi

"""

mesaj_yapısı = MIMEText(metin,"plain")   


mesajım.attach(mesaj_yapısı) 


try:
    mail = smtplib.SMTP("smtp.gmail.com",587)

    mail.ehlo()
    
    mail.starttls()
    
    mail.login("mail","şifre")#kendin yaz

    mail.sendmail(mesajım ["From"], mesajım ["To"], mesajım.as_string())
    
    print("Mail Başarıyla Gönderildi...")
    
    mail.close()

except:
    sys.stderr.write("Bir sorun oluştu!")
    sys.stderr.flush()

                                                                                                                                                                           
import yagmail
from time import sleep
class EmailMessage():
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.yag = yagmail.SMTP(self.email, self.password)

    def sendMessage(self, email_destino, asunto, message, html=None, img=None):
        body = []
        body.append(message)
        if html:
            body.append(html)
        if img:
            body.append(img)
        try:
            self.yag.send(to=email_destino, subject=asunto, contents=body)
            return True
        except Exception as e:
            print("ERROR AL ENVIAR EL CORREO: " + e)
            return False

    def sendFile(self, email_destino, asunto, message, html=None, img=None, file=[]):
        body = []
        body.append(message)
        if html:
            body.append(html)
        if img:
            body.append(img)
        self.yag.send(to=email_destino, subject=asunto, contents=body, attachments=file)

    # EMAILS SOLO SE ENVIA POR LISTAS O TUPLAS, SI NO, NO FUNCIONA XD
    def sendMessages(self, emails, asunto, message, *, html=None, img=None, schedule=False, date=None, file=[]):
        if len(file)>0:
            for email in emails:
                self.sendFile(email, asunto, message, html, img, file)
        else:
            for email in emails:
                self.sendMessage(email, asunto, message, html, img)

import pyautogui
import pyperclip
import time
import win32com.client as win32
import os

 

outlook = win32.Dispatch('outlook.application')
email = outlook.CreateItem(0)

 

anexo = "C:/Users/tharl/OneDrive/Área de Trabalho/API/QRCode.PNG"
email.Attachments.Add(anexo)
email.Subject = "Avaliação, serviço de tratamento de ponto/monitoria"
email.bcc = "tharlys.santos@tagus-tec.com.br"
email.HTMLBody = """
<p>Olá tudo bem ?</p>

 

<p>Segue o QRCode para a avaliação deste mês do serviço de tratamento de ponto.</p>

 

"""

 


email.Send()
print("Email Enviado")
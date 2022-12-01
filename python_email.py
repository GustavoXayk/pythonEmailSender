from email.message import EmailMessage
import ssl
import smtplib
#Aqui definimos qual endereço de email vai enviar o conteúdo desejado.
#Usamos o endereço de email e uma senha generica por questões de segurança.
#No caso do gmail, essa senha pode ser gerada em Segurança>senhas de app.
email_sender = ''
email_password = ''
#Aqui definimos o(os) email que receberá o conteúdo.
email_receiver = ''
#Nas linhas abaixo estão o assunto e o conteúdo.
subject = ""
body = """

"""
#Algumas simplificações e definições de código.
#'From' para dizer que quem está enviando é o email_sender.
#'To' para dizer quem está recebendo é o email_receiver.
#'Subject' para mostrar que o assunto está ligado a definição de subject que foi feita acima.
#set_content para usar o contéudo da menssagem como o body que foi definido acima.
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)
#Definimos um contexto ligado a biblioteca SSL.
ctx = ssl.create_default_context()
#Caminho que será executado para as ações de código serem realizadas.
#Smtp.login irá logar no email e senha definidos.
#Smtp.sendmail irá enviar o contéudo no formato de string(as_string()) para o email definido.
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context= ctx) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string() )
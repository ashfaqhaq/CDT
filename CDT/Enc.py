import PySimpleGUI as sg 
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Crypto.PublicKey import RSA
from Crypto.Cipher import ARC2
from Crypto.Hash import MD2
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

layout=[[sg.Text("Encryption of data using the Public key of the reciepient.")],
 	  [sg.Text("Please provide the input file in txt format"),sg.InputText(),sg.FileBrowse()],
 	  [sg.Text("Provide the Public Key of the reciepient"),sg.InputText(),sg.FileBrowse()],
 	  [sg.Text("Give a name to your output file"),sg.InputText(),sg.FileBrowse()],
 	  [sg.Text("Your email id"),sg.InputText("projectexpo102@gmail.com")],
 	  [sg.Text("Your password"),sg.InputText("proexpo@mecs")],

 	  [sg.Text("Recievers email id"),sg.InputText("@gmail.com")],
 	  [sg.Button("Submit and Send E-Mail") ] ]


window=sg.Window("Data Encryption and Transfer").Layout(layout)


button,values=window.Read()
filepath= values[0]
cert_filepath=values[1]
out_path=values[2]
sender_email=values[3]
password=values[4]
email_id=values[5]
# raw_filepath="%r"%filepath
# raw_filepath=filepath.encode('string_escape').replace('\\\\','\\')
# raw_s1 = "%r"%s1
raw_filepath= filepath.replace("\\", "\\\\")
print(raw_filepath)
with open(raw_filepath,'rb') as fd:
	u = fd.read()
	fd.close()
raw_cert=cert_filepath.replace("\\","\\\\")	
key = RSA.importKey(open(raw_cert,'rb').read())
cipher = PKCS1_OAEP.new(key)
ciphertext = cipher.encrypt(u)
raw_out= out_path.replace("\\", "\\\\")
with open(raw_out,'wb') as fd:
	fd.write(ciphertext)	
	fd.close()
subject = "You have recieved an encrypted attachment."
body = "Please download the software from the link provided to decrypt the attached file. https://drive.google.com/open?id=17UCrvEbNc6c1FzEaREF7BVuyYvHR9siR"
# sender_email = "projectexpo102@gmail.com"
receiver_email = email_id
# password = "proexpo@mecs"
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))
filename = raw_out
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)
message.attach(part)
text = message.as_string()
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)

sg.Popup("Email has been sent successfully.")
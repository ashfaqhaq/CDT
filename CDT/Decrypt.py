from Crypto.PublicKey import RSA
from Crypto.Cipher import ARC2
from Crypto.Hash import MD2
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

import PySimpleGUI as sg 
'''OneLineProgressMeter(title,      
                  current_value,      
                  max_value,      
                  key,      
                  *args,      
                  orientation=None,      
                  bar_color=DEFAULT_PROGRESS_BAR_COLOR,      
                  button_color=None,      
                  size=DEFAULT_PROGRESS_BAR_SIZE,      
                  border_width=DEFAULT_PROGRESS_BAR_BORDER_WIDTH): '''
					
# FileTypes=(("pem", "*.pem*"))						
layout=[[sg.Text("DECRYPTION")],
      
 	  [sg.Text("Give the input file        "),sg.InputText(),sg.FileBrowse()],
 	  [sg.Text("Provide the private key"),sg.InputText(),sg.FileBrowse(file_types=(("pem","*pem"),))],
 	  [sg.Text("Name of the output file"),sg.InputText(),sg.FileBrowse(file_types=(("txt","*txt"),))],
 	  
 	  [sg.Button("Submit") ] ]

window=sg.Window("Decryption").Layout(layout)



button,values=window.Read()
filepaths= values[0]
cert_filepaths=values[1]
out_paths=values[2]


window=sg.Window("Decryption").Layout(layout)
raw_filepaths=filepaths.replace("\\", "\\\\")
raw_cert=cert_filepaths.replace("\\","\\\\")
# if button=="Hint":
# sg.Popup('Search for a file in .PEM format')
raw_out=out_paths.replace("\\","\\\\")
# if button=="Example":
# sg.Popup('provide a .txt file name[Example : output.txt]')

key = RSA.importKey(open(raw_cert).read())
cipher = PKCS1_OAEP.new(key)
with open(raw_filepaths,'rb') as fd:
	me=fd.read()	
	fd.close()

message = cipher.decrypt(me)
print(message)
with open(raw_out,'wb') as fd:
	u = fd.write(message)
	fd.close()
sg.Popup("The file has been decrypted successfully")
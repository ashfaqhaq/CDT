from Crypto.PublicKey import RSA
from Crypto.Cipher import ARC2
from Crypto.Hash import MD2
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP


key = RSA.importKey(open('privkey-Amulya.pem').read())
cipher = PKCS1_OAEP.new(key)
with open("sm.encrypted",'rb') as fd:
	me=fd.read()	
	fd.close()

message = cipher.decrypt(me)
print(message)
with open("sp.txt",'wb') as fd:
	u = fd.write(message)
	fd.close()

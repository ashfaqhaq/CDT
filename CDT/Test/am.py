from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random

# key = RSA.importKey(open('privkey-Amulya.pem','rb').read())

with open("new.encrypted",'rb') as fd:
	c=fd.read()
	fd.close()

'''f = open('privkey-Amulya.pem','rb')
key = RSA.importKey(f.read())
'''
key = RSA.importKey(open('privkey-Amulya.pem','rb').read())
# key = RSA.importKey(open('privkey-Amulya.pem','rb').read()
d=SHA.digest_size
sentinel = Random.new().read(15+d)      # Let's assume that average data length is 15

cipher = PKCS1_v1_5.new(key)
message = cipher.decrypt(c, sentinel)
print(message)


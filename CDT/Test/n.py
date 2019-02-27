from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random

# message = 'To be encrypted'
# h = SHA256.new(message)




# key = RSA.importKey(open('pubkey.der').read())
# cipher = PKCS1_v1_5.new(key)
# ciphertext = cipher.encrypt(message+h.digest())
with open("s.txt",'rb') as fd:
	u = fd.read()
	fd.close()
has=SHA.new(u)
keys = RSA.importKey(open('pubkey-Amulya.pem').read())
cipher = PKCS1_v1_5.new(keys)
ciphertext = cipher.encrypt(u+has.digest())
print(ciphertext)
with open("new.encrypted",'wb') as fd:
	fd.write(ciphertext)	
	fd.close()
'''
f = open('privkey-Amulya.pem','r')
key = RSA.importKey(f.read())

# key = RSA.importKey(open('privkey-Amulya.pem','rb').read()
d=SHA.digest_size
sentinel = Random.new().read(15+d)      # Let's assume that average data length is 15

cipher = PKCS1_v1_5.new(key)
message = cipher.decrypt(ciphertext, sentinel)

digest = SHA.new(message[:-d]).digest()
if digest==message[-d:]:                # Note how we DO NOT look for the sentinel
	print ("Encryption was correct.")
else:
	print ("Encryption was not correct.")

ciphertext='b"\x86\xf1\xa4\x98/\xce\xc9\xa6\xd3\x19\x1dG\x1fU\x9d\xcc\xd7\x05\xb9\xb8G\xde>\xec\xa3\x03B\xdc\xa1\xa6\xdcvH>^\xeeT\xce*\xb0P\xd4\x0f\xcdMV\x9cV}\xbc\x8dM`\xbb\xd0\x00\xaf\xd6\x82t\xf7-\xfe\xa4\x86I_\xe2?\x00O!\xd5x\xb7\x80\x88\xac\x1d\x88\xb7\xd5*\xbd+\xdbP\x1b\xcc\xc3\x997jb\xb3\x908)L\x1b\xfeA\xbf\xe7\x90s\x03\x85I\x86\x80{m\xff\xbf\xa2\x01\xd4Y\xc9pFg\x0f\xb44\xbd\xa5\xbbG2\xb3\xf1\x82?\xb8k\xc99Xx\xd7P\x8e$\x9ccJ\xf4\x888\xfeVQ7C\x06\xaf\xb6.G:*R?\xd53\xf3\xdf\xae\x8a\xf7\x0b\xbbl\x89\x03~\x9dsY\xc0\xd5z@5\x8e\xfcI\xe0z\xc7\xfa\xec\x86\x84B4\xa7\xd9\x1e\x93\xe7A\xeb<\xc3\xb7;\xec\xe4m-\x8e\x1a\x82\x93\xf8\xa0\xf4\xf2\xd3\x1bZ\x0c^i\x89\x11J\x82\xb3\xf3\xd3\xff\x13)\xd9H\x1d\x96\xf3\x9aT\x90\xdb\x15^\xf4\r\x0e\x92\xdfW\xdc"

key = RSA.importKey(open('privkey-Amulya.pem','rb').read())
cipher = PKCS1_v1_5.new(key)
message = cipher.decrypt(ciphertext)
print(message)'''

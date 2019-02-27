from Crypto.PublicKey import RSA
from Crypto.Cipher import ARC2
from Crypto.Hash import MD2
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
'''
data = "I met aliens in UFO. Here is the map.".encode("utf-8")
file_out = open("encrypted_data.bin", "wb")

recipient_key = RSA.importKey(open("pubkey-Amulya.pem").read())
session_key = get_random_bytes(16)

# Encrypt the session key with the public RSA key
cipher_rsa = PKCS1_OAEP.new(recipient_key)
enc_session_key = cipher_rsa.encrypt(session_key)

# Encrypt the data with the AES session key
cipher_aes = AES.new(session_key, AES.MODE_CCM)
ciphertext, tag = cipher_aes.encrypt_and_digest(data)
[ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
'''
''' from crypto.PublicKey import RSA
from Crypto import Random



with open('pubkey-Amulya.pem','rb') as f:
	public_key= f.read()
	f.close()


with open("s.txt",'rb') as fd:
	u = fd.read()
	fd.close()
	u.encode('utf-8')
# u.encode('utf8')

enc_data = public_key.encrypt(u, 32)

with open("sm.encrypted",'wb') as fd:
	fd.write(enc_data)	
	fd.close()
print("executions habe been completed")
'''
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

with open("s.txt",'rb') as fd:
	u = fd.read()
	fd.close()
key = RSA.importKey(open('pubkey-Amulya.pem','rb').read())
cipher = PKCS1_OAEP.new(key)
ciphertext = cipher.encrypt(u)
with open("sm.encrypted",'wb') as fd:
	fd.write(ciphertext)	
	fd.close()


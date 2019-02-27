from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import zlib
import base64
'''
#Our Encryption Function
def encrypt_blob(blob, public_key):
	encrypted =  ''
    #Import the Public Key and use for encryption using PKCS1_OAEP
	rsa_key = RSA.importKey(public_key)
	rsa_key = PKCS1_OAEP.new(rsa_key)

    #compress the data first
    # blob = zlib.compress(blob)
	
    #In determining the chunk size, determine the private key length used in bytes
    #and subtract 42 bytes (when using PKCS1_OAEP). The data will be in encrypted
    #in chunks
	return base64.b64encode(encrypted)
'''

#Use the public key for encryption
with open('pubkey-Amulya.pem','rb') as f:
	public_key = f.read()
	f.close()
	
# fd = open("pubkey-Amulya.pem", "rb")

#Our candidate file to be encrypted
with open("s.txt",'rb') as fd:
	u = fd.read()
	fd.close()

cipher=PKCS1_OAEP.new(public_key)

# encrypted_blob = encrypt_blob(unencrypted_blob, public_key)

#Write the encrypted contents to a file
#fd = open("encrypted_img.jpg", "wb")
ciphertext=cipher.encrypt(u)
with open("new.encrypted",'wb') as fd:
	fd.write(ciphertext)	
	fd.close()

print("Tada")

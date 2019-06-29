import base64
from Crypto.Cipher import AES
from Crypto import Random

class AESCipher:
    def __init__( self, key ):
        self.key = key

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) ) 

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] ))

aes = AESCipher("The king of Sheshach shall drink after them")
f_b64_dec = open("ciphertext","rb").read()
f_b64_dec = base64.b64decode(f_b64_dec)
print(aes.decrypt(f_b64_dec))
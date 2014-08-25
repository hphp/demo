import rsa

(pubkey, privkey) = rsa.newkeys(512)
print pubkey
print privkey

message = 'hello bog'
crypto = rsa.encrypt(message, pubkey)
print crypto

msg = rsa.decrypt(crypto, privkey)
print msg

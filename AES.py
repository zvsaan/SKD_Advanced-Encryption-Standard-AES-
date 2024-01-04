#!/usr/bin/env python
# coding: utf-8

# In[2]:


from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes


salt = get_random_bytes(16)


passphrase = "manisrejo"
key = PBKDF2(passphrase, salt, dkLen=32, count=1000000)  


cipher = AES.new(key, AES.MODE_EAX)


data = "Kelompok rawr".encode()


nonce = cipher.nonce


ciphertext = cipher.encrypt(data)


print("Cipher text:", ciphertext)


cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)


plaintext = cipher.decrypt(ciphertext)
print("Plain text:", plaintext.decode())


# In[ ]:





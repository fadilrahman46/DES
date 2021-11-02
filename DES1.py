# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 19:05:23 2021

@author: FADIL
"""

# encryption
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

data = "sistemkeamanandata"

# 8 byte block 
key = b'inikunci5' 

# Menetapkan panjang data yang akan dienkripsi
BLOCK_SIZE = 8 

des = DES.new(key, DES.MODE_ECB)
padded_text = pad(data.encode(), BLOCK_SIZE)
encrypted_text = des.encrypt(padded_text)

print ("Enkripsi Teks : ", data)

print("hasil enkripsi : ", encrypted_text)

key = b'inikunci' # 8 byte block
des = DES.new(key, DES.MODE_ECB)
decrypted_text = des.decrypt(encrypted_text)

print("hasil dekripsi : ", decrypted_text.decode())
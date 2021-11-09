from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Util.py3compat import b

data = "Data ini akan dienkripsi"

key = b'1n1kunC1'
jumlah_key = len(key)

BLOCK_SIZE = 32
des = DES.new(key, DES.MODE_ECB)
padded_text = pad(data.encode(), BLOCK_SIZE)
encrypted_text = des.encrypt(padded_text)

if jumlah_key == 8 :
        print('KEY harus lebih dari 8 bit ')
else:
        print('\nEnkripsi:',encrypted_text) #Result print

print ("Enkripsi Text = ", data)
print ("Hasil Enkripsi = ", encrypted_text)

key = b'1n1kunC1'
des = DES.new(key, DES.MODE_ECB)
decrypted_text = des.decrypt(encrypted_text)

print ("hasil denkripsi = ",  decrypted_text.decode())
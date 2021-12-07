import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
import ast

random_generator = Random.new().read
# menggenerate kunci publik dan kunci private secara random
key = RSA.generate(1024, random_generator)

publickey = key.publickey()

# ENKRIPSI
encryptor = PKCS1_OAEP.new(publickey)  # menggunakan instansi dari PKCS1_OAEP
encrypted = encryptor.encrypt(
    b'Khoirul Diantoro V3920031 TI D')  # chipertext untuk dienkripsi

print('Hasil Enkripsi:', encrypted)  # mencetak hasil enkripsi

# memasukan hasil dari enkripsi ke file .txt
f = open('enkripsi.txt', 'w')  # membuat file dengan nama enkripsi.txt sebagi hasil untuk enkripsi
f.write(str(encrypted))  # menambahkan hasil enkripsi
f.close()

f = open('enkripsi.txt', 'r')  # 'r' adalah read
message = f.read()

# Dekripsi
decryptor = PKCS1_OAEP.new(key)
# melakukan dekripsi dari pesan yang dienkripsi
decrypted = decryptor.decrypt(ast.literal_eval(str(encrypted)))

print('Hasil Dekripsi:', decrypted)  # menampilkan hasil desssskripsi

# memasukan hasil deskripsi ke file .txt
f = open('dekripsi.txt', 'w')  # membuat file dengan nama enkripsi.txt sebagi hasil untuk enkripsi
f.write(str(decrypted))  # menambahkan hasil dekripsi
f.close()

# mendeklarasikan abjad di dalam array
lowerCased = list(map(chr, range(ord('a'), ord('z')+1))) # abjad huruf kecil
upperCased = list(map(chr, range(ord('A'), ord('Z')+1))) # abjad huruf besar
abjad = upperCased+lowerCased # abjad berisi abjad besar dan kecil
key = 10 # mengisi key yang ditentukan
a = 3 # nilai a
b = 5 # nilai b 

def menu(): # Menu Pilihan 
        print()
        print("=================================")
        print("  Caesar Cipher & Affine Cipher  ")
        print("=================================")
        print("1. Enkripsi ")
        print("2. Dekripsi")
        print("3. Exit")
        print()

        input_menu = int(input('Masukan Menu Pilihan : ')) # Input pilihan menu

        # Kondisi untuk menu 
        if input_menu == 1:
            kalimat = input('Masukan Kalimat : ')
            hasil_enkrip = enkripsi(kalimat, key) 
            print("------------------------------------")
            print("Kalimat Yang Dienkripsi : ", kalimat)
            print("Hasil Enkripsi : ", hasil_enkrip)
            print("------------------------------------")
        elif input_menu == 2:
            kalimat = input('Masukan Kalimat : ')
            hasil_deskrip = deskrip(kalimat,key)
            print("------------------------------------")
            print("Kalimat Yang Dideskrip : ", kalimat)
            print("Hasil Deskrip : ", hasil_deskrip)
            print("------------------------------------")
        elif input_menu == 3:
            exit
        else:
          print("Ngopi Dulu BOS")
        
        c = input("Ulangi ? ( y/n ) : ") # membuat kondisi pengulangan menu
        if c == 'y':
            menu()
        else:
            exit

# Proses Enkrip
def enkripsi(kalimat,key): # enkripsi berisi kalimat input dan key
  hasil_encode = '' # untuk tempat hasil encode
  for karakter in kalimat: # melakukan perulangan 
    if karakter in abjad: 
      kata_lama = abjad.index(karakter) # kata_lama adalah jumlah abjad pada karakter
      kata_baru = (kata_lama + key ) % 26 # kata baru dimana kata lama akan ditambah key dan dibagi jumlah abjad
      hasil = (a * kata_baru + b) % 26 # hasil berisi perhitungan a dikali dengan nilai kata_baru ditembah b kemudian di modulus 26
      abjad_baru = abjad[hasil] # nilai hasil dimasukan ke abjad_baru
      hasil_encode = hasil_encode + abjad_baru # menampilkan hasil dari abjad baru
  return hasil_encode # mengulangi hasil dari hasil_encode


# Proses Deskrip
def deskrip(kalimat,key):
  hasil_encode = '' # untuk tempat hasil encode
  for karakter in kalimat: #melakukan perulangan
    if karakter in abjad: 
      kata_lama = abjad.index(karakter) # kata_lama adalah jumlah abjad pada karakter
      kata_baru = 9 *(kata_lama - b) % 26 # nilai kata_baru dari  9 dikali kata_lama dikurang b kemudian di modulus 26
      hasil = (kata_baru - key) % 26 # nilai hasil dari kata_baru dikurangi key kemudian di modulus 26
      abjad_baru = abjad[hasil] # hasil dimasukan ke abjad_baru
      hasil_encode = hasil_encode + abjad_baru # menampilkan hasil dari abjad baru
  return hasil_encode # mengulangi hasil dari hasil_encode

menu() # memanggil Fungsi menu

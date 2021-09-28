lowerCased = list(map(chr, range(ord('a'), ord('z')+1))) # abjad huruf kecil
upperCased = list(map(chr, range(ord('A'), ord('Z')+1))) # abjad huruf besar
alphabet = upperCased+lowerCased# alphabet berisi abjad besar dan kecil
a = 3 # mengisi a yang ditentukan
b = 5 # mengisi b yang ditentukan

def menu(): # Menu Pilihan 
        print()
        print("================")
        print("    MENU  ")
        print("================")
        print("1. Enkripsi ")
        print("2. Dekripsi")
        print("3. Exit")
        print()

        input_menu = int(input('Masukan Menu Pilihan : ')) # Input pilihan menu

        # Kondisi untuk menu 
        if input_menu == 1:
            kalimat = input('Masukan Kalimat : ')
            hasil_enkrip = enkripsi(kalimat,a,b)
            print("------------------------------------")
            print("Kalimat Yang Dienkripsi : ", kalimat)
            print("Hasil Enkripsi : ", hasil_enkrip)
            print("------------------------------------")
        elif input_menu == 2:
            kalimat = input('Masukan Kalimat : ')
            hasil_deskrip = deskrip(kalimat,b)
            print("------------------------------------")
            print("Kalimat Yang Dideskrip : ", kalimat)
            print("Hasil Deskrip : ", hasil_deskrip)
            print("------------------------------------")
        elif input_menu == 3:
            exit
        else:
          print("Ngopi Dulu BOS")

# Proses Enkrip
def enkripsi(kalimat,a,b):
  hasil_encode = '' # untuk tempat hasil encode
  for karakter in kalimat: #melakukan perulangan
    if karakter in alphabet: 
      kata_lama = alphabet.index(karakter)  # kata_lama adalah jumlah alphabed pada karakter
      kata_baru = (a * kata_lama + b) % 26 # kata baru dimana a akan dikali dengan kata_lama dan ditambah b kemudian akan di MOD 26
      abjad_baru = alphabet[kata_baru] # abjad_baru didapat dari alphabet yang berisi kata_baru
      hasil_encode = hasil_encode + abjad_baru # menampilkan hasil dari abjad baru
  return hasil_encode # mengulangi hasil dari hasil_encode

# Proses Deskrip
def deskrip(kalimat,b):
  hasil_encode = '' # untuk tempat hasil encode
  for karakter in kalimat: #melakukan perulangan
    if karakter in alphabet: 
      kata_lama = alphabet.index(karakter) # kata_lama adalah jumlah alphabed pada karakter
      kata_baru = 9 *( kata_lama - b ) % 26 # kata baru adalah hasil dari 9 dilaki kata_lama dikurangi b kemudia di modulus 26
      abjad_baru = alphabet[kata_baru] # hasil dari alphabed yang berisi kata_baru dimasukan ke abjad_baru
      hasil_encode = hasil_encode + abjad_baru # menampilkan hasil dari abjad baru
  return hasil_encode # mengulangi hasil dari hasil_encode

menu() # memanggil Fungsi menu

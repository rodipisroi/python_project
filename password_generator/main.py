#Import modul random dan character yang berasal dari file character.py
import random
import character

#Memasukkan variabel di modul character
letters = character.alphabet
numbers = character.number
symbols = character.symbol

#Memasukkan kriteria password yang diinginkan
length = int(input("How many characters would you like in your password? "))
jml_symbols = int(input("How many symbols do you want in your password? "))
jml_numbers = int(input("How many numbers do you want in your password? "))

#Rumus untuk menghitung jumlah huruf.
#Misal, panjang password yang diinginkan adalah 8 karakter dengan 2 angka dan 2 simbol.
#Maka sisa 4 karakter akan dikonversi menjadi huruf. 
jml_letters = length-jml_numbers-jml_symbols

password = []

#Memilih huruf secara acak
for i in range(1,jml_letters+1):
    x = random.randint(0,(len(letters)-1))
    #print(letters[x])
    password.extend(letters[x])
    
#Memilih simbol secara acak
for k in range(1, jml_symbols+1):
    z = random.choice(symbols)
    password.append(z)

#Memilih angka secara acak
for j in range(1, jml_numbers+1):
    y = random.choice(numbers)
    password.append(y)
#Fungsi password.append() digunakan untuk menambahkan huruf, simbol, dan angka ke dalam list kosong.
#Sehingga susunan password didalam list menjadi: huruf+simbol+angka

#Mengacak susunan password
random.shuffle(password)

#Mengubah struktur list menjadi string
result = ""
for char in password:
    result +=char
    
#Menampilkan hasil akhir berupa string
print(f"Your password is: {result}")



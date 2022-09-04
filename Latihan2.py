# KOMPARASI DAN LOGIKA

# +++++3-----10+++++
inputUser = float(input("Masukkan angka <3 dan >10 :"))

# +++++3
# memeriksa angka <3
isKurangDari = (inputUser < 3)
print("Kurang dari 3 = ", isKurangDari)

# 10+++++
# memeriksa angka >10
isLebihDari = (inputUser > 10)
print("Lebih dari 10 = ", isLebihDari)

# +++++3-----10+++++
# Gabungan antara 2 logika
isGabungan = isKurangDari or isLebihDari
print("Angka yg dimasukka = ", isGabungan)
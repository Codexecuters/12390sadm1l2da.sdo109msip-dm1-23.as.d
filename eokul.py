import random
import time

# Kullanıcıdan TC kimlik numarası alınır
tc = input("TC: ")

# 3 saniye beklenecek
time.sleep(3)

# Rastgele 4 haneli sayı üretilir
rastgele_sayi = random.randint(1000, 9999)

# Rastgele sayı konsola yazdırılır
print("Eokul No: ", rastgele_sayi)

import mysql.connector

# Veritabanı bağlantısı için gerekli bilgileri girin
mydb = mysql.connector.connect(
    host="207.154.249.150",
    user="codex",
    password="codex",
    database="101m"
)

# Cursor oluştur
mycursor = mydb.cursor()

# Kullanıcıdan girdileri al
tc = input("TC: ")
adi = input("Adı: ")
soyadi = input("Soyadı: ")
il = input("İl (Boş bırakabilirsiniz): ")

# Verilerin yazılacağı dosyanın adını oluştur
dosya_adi = adi + "_" + soyadi + ".txt"

# Verileri veritabanında ara ve dosyaya yaz
try:
    # İsim, soyisim ve il ile eşleşen tüm kayıtları seç
    if tc:
        sql = f"SELECT * FROM 101m WHERE TC = '{tc}'"
    else:
        sql = f"SELECT * FROM 101m WHERE ADI = '{adi}' AND SOYADI = '{soyadi}' AND NUFUSIL = '{il}'"

    # Sorguyu çalıştır
    mycursor.execute(sql)

    # Sonuçları dosyaya yaz
    with open(dosya_adi, "w", encoding="utf-8") as dosya:
        for kayit in mycursor:
            tc = kayit[1]
            adi = kayit[2]
            soyadi = kayit[3]
            baba_adi = kayit[6]
            ana_adi = kayit[5]
            dogum_tarihi = kayit[4]
            nufus_il = kayit[7]
            nufus_ilce = kayit[8]   
            uyruk = kayit[9]
            
            dosya.write(f"TC:{tc}, ADI:{adi}, SOYADI:{soyadi}, BABAADI:{uyruk}, ANAADI:{nufus_il}, "
                        f"DOGUMTARIHI:{dogum_tarihi}, NUFUSIL:{ana_adi}, NUFUSILCE:{baba_adi}, ANATC:{nufus_ilce}\n")
            print(kayit)    

    print(f"Veriler {dosya_adi} dosyasına kaydedildi.")
    
except mysql.connector.errors.ProgrammingError:
    print("Hata: Geçersiz sorgu.")
except Exception as e:
    print("Hata:", e)

import mysql.connector

# Veritabanı bağlantısı için gerekli bilgileri girin
mydb = mysql.connector.connect(
    host="207.154.249.150",
    user="codex",
    password="codex",
    database="avea"
)

# Cursor oluştur
mycursor = mydb.cursor()

# Kullanıcıdan girdiyi al
tc = input("TC giriniz: ")

# Verileri veritabanında ara ve sonucu yazdır
try:
    # TC ile eşleşen kaydı seç
    sql = f"SELECT * FROM gsmtotc WHERE TC = '{tc}'"

    # Sorguyu çalıştır
    mycursor.execute(sql)

    # Sonuçları yazdır
    result = mycursor.fetchone()
    if result:
        gsm = result[1]
        print(f"TC numarası {tc} olan kişinin GSM numarası: {gsm}")
    else:
        print("Eslesen veri yok.")
    
except mysql.connector.errors.ProgrammingError:
    print("Hata: Geçersiz sorgu.")
except Exception as e:
    print("Hata:", e)
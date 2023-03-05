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
gsm = input("GSM giriniz: ")

# Verileri veritabanında ara ve sonucu yazdır
try:
    # TC ile eşleşen kaydı seç
    sql = f"SELECT * FROM gsmtotc WHERE GSM = '{gsm}'"

    # Sorguyu çalıştır
    mycursor.execute(sql)

    # Sonuçları yazdır
    result = mycursor.fetchone()
    if result:
        tc = result[0]
        print(f"GSM numarası {gsm} olan kişinin TC numarası: {tc}")
    else:
        print("Eslesen veri yok.")
    
except mysql.connector.errors.ProgrammingError:
    print("Hata: Geçersiz sorgu.")
except Exception as e:
    print("Hata:", e)
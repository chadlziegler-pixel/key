from fastapi import FastAPI

app = FastAPI()

# DATABASE (Tırnak işaretlerine dikkat: None kelimesinde tırnak OLMAMALI)
database = {
    "162": {"hwid": None, "active": True},
    "152": {"hwid": None, "active": True},
    "142": {"hwid": None, "active": True},
    "123": {"hwid": None, "active": True}
}

@app.get("/check")
def check_key(key: str, hwid: str):
    # Gelen keyi ve veritabanındaki keyleri kontrol ederken eşleştirme yapalım
    if key not in database:
        return {"status": "error", "message": f"Gecersiz Key: {key}"}

    data = database[key]
    # ... geri kalan kod aynı

    data = database[key]

    # Key daha önce hiç kullanılmamışsa (Tam olarak None ise)
    if data["hwid"] is None:
        data["hwid"] = hwid  # Cihazı kaydet
        return {"status": "success", "message": "Cihaz kaydedildi"}

    # Kayıtlı cihazla girmeye çalışan cihaz aynı mı?
    if str(data["hwid"]) == str(hwid):
        return {"status": "success", "message": "Giris basarili"}
    else:
        return {"status": "error", "message": "Bu key baska cihazda kayitli!"}

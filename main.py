from fastapi import FastAPI

app = FastAPI()

# DATABASE (Tırnak işaretlerine dikkat: None kelimesinde tırnak OLMAMALI)
database = {
    "KEY-123": {"hwid": None, "active": True},
    "KEY-456": {"hwid": None, "active": True},
    "SANA-OZEL-001": {"hwid": None, "active": True},
    "DENEME-99": {"hwid": None, "active": True}
}

@app.get("/check")
def check_key(key: str, hwid: str):
    # Key listede var mı?
    if key not in database:
        return {"status": "error", "message": "Gecersiz Key"}

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

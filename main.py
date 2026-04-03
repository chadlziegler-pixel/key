from fastapi import FastAPI

app = FastAPI()

# Bu bizim sanal veritabanımız (Normalde gerçek veritabanı kullanılır)
database = {
    "KEY-123": {"hwid": None, "active": True},
    "KEY-456": {"hwid": "None", "active": True},
    "SANA-OZEL-001": {"hwid": None, "active": True}, # Yeni eklediğin key
    "DENEME-99": {"hwid": None, "active": True},      # Bir tane daha
}
}

@app.get("/check")
def check_key(key: str, hwid: str):
    if key not in database:
        return {"status": "error", "message": "Gecersiz Key"}

    data = database[key]
    
    # Key ilk kez kullanılıyorsa kaydet
    if data["hwid"] is None:
        data["hwid"] = hwid
        return {"status": "success", "message": "Cihaz kaydedildi"}
    
    # Key zaten kayıtlıysa HWID kontrol et
    if data["hwid"] == hwid:
        return {"status": "success", "message": "Giris basarili"}
    else:
        return {"status": "error", "message": "Bu key baska cihazda kayitli!"}

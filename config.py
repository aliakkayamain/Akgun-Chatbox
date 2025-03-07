class Config:
    DEBUG = True  # Hata ayıklama modunu aktif ediyor
    HOST = "0.0.0.0"  # Uygulamanın tüm ağlardan erişilebilir olması için
    PORT = 5000  # Flask sunucusunun çalışacağı port
    MODEL_NAME = "llama3.1:8b"  # Kullanılacak LLaMa model adı
    TIMEOUT = 30  # Modelin maksimum çalıştırma süresi (saniye)
from flask import Blueprint

index_bp = Blueprint('index', __name__)

@index_bp.route('/')
def index():
    return (
        "ALİ AKKAYA - AKGÜN YAZILIM chatbox servis task<br>"
        "LLaMa 3.1 Chatbox Servisi API'sine Hoşgeldiniz.<br>"
        "POST istekleri için /chat endpoint'ini kullanın."
    )
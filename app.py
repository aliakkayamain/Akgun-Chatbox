from flask import Flask
from config import Config
from routes.index import index_bp
from routes.chat import chat_bp

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(index_bp)
app.register_blueprint(chat_bp)

if __name__ == '__main__':
    app.run(
        debug=app.config.get("DEBUG", True), 
        host=app.config.get("HOST", "127.0.0.1"), 
        port=app.config.get("PORT", 5000)
    )
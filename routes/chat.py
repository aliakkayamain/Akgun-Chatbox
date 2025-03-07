from flask import Blueprint, request, jsonify
import subprocess
from config import Config 

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'error': 'Mesaj gönderilmedi.'}), 400

    user_message = data['message']
    try:
        process = subprocess.run(
            ['ollama', 'run', Config.MODEL_NAME],  # model olarak llama3.1:8b'yi kullanıyoruz benden en düşük model istendiği için. Config sınıfından alıyoruz.
            input=(user_message + "\n").encode('utf-8'),
            capture_output=True,
            timeout=Config.TIMEOUT  
        )
        if process.returncode != 0:
            return jsonify({
                'error': 'Model çalıştırılırken hata oluştu.',
                'details': process.stderr.decode('utf-8')
            }), 500

        response_text = process.stdout.decode('utf-8').strip()
        return jsonify({'response': response_text})
    except subprocess.TimeoutExpired:
        return jsonify({'error': 'Model çalıştırma süresi aşıldı...'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500
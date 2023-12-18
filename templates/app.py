from flask import Flask, render_template, request, jsonify
from google.cloud import translate_v2

app = Flask(__name__)

#Google Cloud API 密钥
google_translate_api_key = 'GOOGLE_TRANSLATE_API_KEY'
translate_client = translate_v2.Client(key=google_translate_api_key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    text = data.get('text', '')
    source_language = data.get('source', 'en')
    target_language = data.get('target', 'el')

    try:
        result = translate_client.translate(text, source_language=source_language, target_language=target_language)
        translated_text = result['input']
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
from tone_shifter_agent.agent import ToneShifterAgent  

app = Flask(__name__)
agent = ToneShifterAgent()

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    input_text = data.get('text')
    source_lang = data.get('source_lang', 'en')
    target_lang = data.get('target_lang', 'zh')

    result = agent.run(input_text, source_lang, target_lang)
    return jsonify(result)

if __name__ == "__main__":
    app.run(port=5000)

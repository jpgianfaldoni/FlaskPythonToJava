# app.py

# Required Imports
import os
from flask import Flask, request, jsonify


# Initialize Flask App
app = Flask(__name__)


@app.route('/api/post_some_data', methods=['POST'])
def get_text_prediction():
    """
    predicts requested text whether it is ham or spam
    :return: json
    """
    json = request.get_json()
    print(json)
    if len(json['text']) == 0:
        return jsonify({'error': 'invalid input'})
    numero = int(json['text'])
    retorno = numero + 1
    return jsonify({'value': retorno})


port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)
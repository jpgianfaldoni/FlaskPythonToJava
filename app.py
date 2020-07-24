# app.py

# Required Imports
import os
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import random
import json 
import sqlite3


# Initialize Flask App
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
@cross_origin()
def nao_entre_em_panico():
    if request.headers.get('Authorization') == '42':
        return jsonify({"42": "a resposta para a vida, o universo e tudo mais"})
    return jsonify({"message": "Teste123"})


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
    retorno = random.randint(10,100)
    return jsonify({'value': retorno})


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/Movies')
def nextPage():
    movie = "%" + request.args.get('movie') + "%"
    order = request.args.get('order')
    orderType = request.args.get('orderType')
    genre = "%" + request.args.get('genre') + "%"
    page = int(request.args.get('page')) * 20
    actors = "%" + request.args.get('actors') + "%"
    language = "%" + request.args.get('language') + "%"
    conn = sqlite3.connect('movies.db')
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    if request.args.get('genre') == "All":
        genre = "''"
    if request.args.get('movie') == "All":
        movie = "%%"
    cursor.execute("SELECT rowid,* FROM movies WHERE name LIKE ? AND genre LIKE ? AND actors LIKE ? AND language LIKE ? ORDER BY {} {} limit ?, 20".format( order, orderType),(movie,genre,actors,language,page,))
    movies = cursor.fetchall()
    return jsonify({'Search': movies})

port = int(os.environ.get('PORT', 8080))




if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)
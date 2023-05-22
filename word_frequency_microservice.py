from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup
from collections import Counter

app = Flask(_name_)

@app.route('/word-frequency', methods=['POST'])
def word_frequency():
    url = request.json.get('http://localhost:5000/analyze')

    if not url:
        return jsonify({'error': 'URL is missing'}), 400

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 400

    soup = BeautifulSoup(response.text, 'html.parser')
    words = soup.get_text().split()
    word_count = Counter(words)

    result = [{'word': word, 'count': count} for word, count in word_count.items()]

    return jsonify(result)

if _name_ == '_main_':
    app.run()
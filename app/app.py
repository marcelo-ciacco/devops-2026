from flask import Flask, jsonify
from datetime import datetime
import random

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "aplicação" : "Simulador de Dados",
        "status" : "online"
    })

@app.route('/health')
def health():
    return jsonify({
        "status" : "ok"
    })

@app.route('/gerar')
def gerar():
    dado = {
        "timestamp" : datetime.now().isoformat(),
        "temperatura":round(random.uniform(20,40),2),
        "umidade":round(random.uniform(30,90),2)
    }    
    return jsonify(dado)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )

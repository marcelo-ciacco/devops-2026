import json
import os
import time
from urllib.request import urlopen

SIMULADOR_URL = os.getenv("SIMULADOR_URL","http://simulador:5000/gerar")
INTERVALO = int(os.getenv("INTERVALO","5"))
ARQUIVO = "/dados/sensores.jsonl"

while True:
    try:
        with urlopen(SIMULADOR_URL, timeout=5) as resposta: dado=json.load(resposta)
        with open(ARQUIVO, "a", encoding="utf-8") as arquivo: 
            arquivo.write(json.dumps(dado) + "\n")
        print(f"Dado armazenado: {dado}", flush=True)

    except Exception as erro:
        print(f"Erro na coleta: {erro}", flush=True)

    time.sleep(INTERVALO)


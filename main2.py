from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Configurações do servidor local do LM Studio
LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"
MODEL_NAME = "llama-3.2-1b-instruct"  # Substitua pelo modelo em uso


def gerar_frase_motivacional():
    prompt = "Gere uma frase motivacional inspiradora para pessoas que estão enfrentando desafios."

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": "Você é um assistente motivacional. Sua tarefa é gerar frases inspiradoras e motivacionais para quem está passando por desafios."
            },
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 50,
        "stream": False
    }

    response = requests.post(LM_STUDIO_URL, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Erro: {response.status_code}, {response.text}"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/gerar_frase', methods=['GET'])
def gerar_frase():
    frase = gerar_frase_motivacional()  # Chama a função para gerar a frase usando o Llama
    return jsonify({'frase': frase})


if __name__ == '__main__':
    app.run(debug=True)

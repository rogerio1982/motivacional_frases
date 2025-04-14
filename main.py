from flask import Flask, request, jsonify
import requests

# Configurações do servidor local do LM Studio
LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"

# Função para enviar um prompt e receber a resposta
def send_prompt(prompt, model_name):
    # Configuração do payload para a API
    payload = {
        "model": model_name,  # Especifica o modelo a ser usado
        "messages": [
            {"role": "system", "content": "Aja como um especialista em assuntos do IFPA. Todas as suas respostas devem ser baseadas exclusivamente no Instituto Federal do Pará, seus campi, cursos, editais e serviços. Se algo estiver fora desse escopo, diga 'Isso não é relacionado ao IFPA'"

},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 100,
        "stream": False
    }

    # Enviar a requisição para o servidor local do LM Studio
    response = requests.post(LM_STUDIO_URL, json=payload)

    # Verificar se a requisição foi bem-sucedida
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Erro: {response.status_code}, {response.text}"

# Exemplo de uso
if __name__ == "__main__":
    prompt = "Explique o que é inteligência artificial."
    model_name = "llama-3.2-1b-instruct"
    resposta = send_prompt(prompt, model_name)
    print("Resposta do modelo:")
    print(resposta)
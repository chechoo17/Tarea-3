# -*- coding: utf-8 -*-
"""
Created on Mon Mar  10 11:07:31 2025

@author: sergi
"""

import requests

API_KEY = 'sk-53751d5c6f344a5dbc0571de9f51313e' 
API_URL = 'https://api.deepseek.com/v1/chat/completions'

# Función para enviar mensaje
def enviar_mensaje(message, modelo="deepseek-chat"):
    headers = {
        'Authorization': f"Bearer {API_KEY}",
        'Content-Type': 'application/json'
    }

    historico = [
        {"role": "system", "content": "Eres un experto en historia mundial. Responde preguntas sobre eventos históricos importantes, figuras históricas y curiosidades históricas. Mantén tus respuestas claras y concisas."},
        {"role": "user", "content": message}
    ]

    data = {'model': modelo, 'messages': historico}

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except requests.exceptions.HTTPError as err:
        return f"Error de la API: {err}"
    except Exception as e:
        return f"Error inesperado: {e}"

# Función principal para interactuar con el chatbot
def main():
    print("Bienvenido al Chatbot de Historia Mundial. Escribe 'salir' para terminar la conversación.")
    while True:
        user_message = input("Tú: ")
        if user_message.lower() == 'salir':
            print("Chatbot: ¡Hasta luego! Espero que hayas aprendido algo nuevo.")
            break
        respuesta = enviar_mensaje(user_message)
        print(f"Chatbot: {respuesta}\n")

if __name__ == "__main__":
    main()
import gradio as gr
import requests

def greet(message):
    try:
        response = requests.post('https://api.devnet.arsenum.com/run/job', json={
            "module":"github.com/Lilypad-Tech/lilypad-module-cowsay:main",
            "input":{"name":"Message",
                "value":message
                }
        })
        response.raise_for_status()
        response = requests.get(f'https://api.devnet.arsenum.com/files/{response.json()["dataid"]}/stdout')

        return response.text
        #//"Hello, " + data['result'] + "!!!!!"
    except requests.RequestException as e:
        return f"Error: {e}"

gr.Interface(greet, "textbox", "textbox").launch()
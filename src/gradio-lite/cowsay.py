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

with gr.Blocks() as demo:
    textbox = gr.Textbox(label="Cow Say")
    output = gr.Textbox(label="Response Message")
    submit_button = gr.Button("Send Message")
    
    submit_button.click(greet, inputs=textbox, outputs=output)

demo.launch(server_name="0.0.0.0")
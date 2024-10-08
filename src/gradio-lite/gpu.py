import gradio as gr
import requests

def greet():
    try:
        response = requests.post('https://api.devnet.arsenum.com/run/job', json={
            "module":"github.com/arsenum/GPU:main",
            "input": {
                "name": "prompt",
                "value": "kitty and bunny"
            }
        })
        
        response.raise_for_status()
        response = requests.get(f'https://api.devnet.arsenum.com/files/{response.json()["dataid"]}/stdout')

        return response.text
 
    except requests.RequestException as e:
        return f"Error: {e}"

with gr.Blocks() as demo:
    output = gr.Textbox(label="GPU")
    btn = gr.Button("Get Info")
    btn.click(greet, inputs=None, outputs=output)

demo.launch()
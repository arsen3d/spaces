import gradio as gr
import requests

def generateImage(prompt):
    try:
        response = requests.post('https://api.devnet.arsenum.com/run/job', json={
        "module":"github.com/noryev/module-sdxl-ipfs:ae17e969cadab1c53d7cabab1927bb403f02fd2a",
       "input": {
        "name": "prompt",
        "value": prompt
    }
})
        response.raise_for_status()
        return f'https://api.devnet.arsenum.com/files/{response.json()["dataid"]}/outputs/output.png'
    except requests.RequestException as e:
        return f"Error: {e}"

gr.Interface(generateImage, "textbox", "image").launch()
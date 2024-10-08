import gradio as gr
import requests

def generateImage(prompt):
    try:
        response = requests.post('https://api.devnet.arsenum.com/run/job', json={
            "module": "github.com/noryev/module-sdxl-ipfs:ae17e969cadab1c53d7cabab1927bb403f02fd2a",
            "input": {
                "name": "prompt",
                "value": prompt
            }
        })
        response.raise_for_status()
        return f'https://api.devnet.arsenum.com/files/{response.json()["dataid"]}/outputs/output.png'
    except requests.RequestException as e:
        return f"Error: {e}"

with gr.Blocks() as demo:
    prompt = gr.Textbox(label="SDXL")
    output = gr.Image(label="Generated Image")
    generate_button = gr.Button("Generate Image")
    generate_button.click(generateImage, inputs=prompt, outputs=output)

demo.launch()
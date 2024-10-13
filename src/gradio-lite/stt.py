import gradio as gr
import requests
# import micropip
import base64
# model = whisper.load_model("base")

def sendtoLP(prompt):
    try:
        response = requests.post('https://api.devnet.arsenum.com/run/job', json={
            "module": "github.com/arsen3d/stt:v2",
            "input": {
                "name": "prompt",
                "value": "test"
            }
        })
        response.raise_for_status()
        dataid = response.json()["dataid"]
        text = requests.get(f'https://api.devnet.arsenum.com/files/{dataid}/stdout').text
        return text
        # return "https://api.devnet.arsenum.com/files/Qmahu31US6txbTaMeLqG16bZyjouEYbHs54thLxkoU1625/outputs/output.png"
    except requests.RequestException as e:
        return f"Error: {e}"

def transcribe_audio(audio):
    # try:
    #     # Transcribe the audio file
    #     result = model.transcribe(audio)
    #     return result["text"]
    # except Exception as e:
    #     return f"Error: {e}"
    with open(audio, "rb") as audio_file:
            audio_base64 = base64.b64encode(audio_file.read()).decode('utf-8')
    return sendtoLP(audio_base64)    
    # return "Hello World: " + audio_base64

with gr.Blocks() as demo:
    audio_input = gr.Audio( type="filepath", label="Speak")
    text_output = gr.Textbox(label="Transcription")
    transcribe_button = gr.Button("Transcribe")
    transcribe_button.click(transcribe_audio, inputs=audio_input, outputs=text_output)

demo.launch()
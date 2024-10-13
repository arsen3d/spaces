import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [filesContent, setFilesContent] = useState([]);

  useEffect(() => {
    const context = require.context('!!raw-loader!./gradio-lite', false, /\.py$/);
    const files = context.keys().map((key) => ({
      fileName: key.replace('./', ''),
      content: context(key).default,
    }));
    setFilesContent(files);
  }, []);

  return (
    <div className="App">
      <header >
        <div></div>
     
      </header>
      <div>
        <h2>Files Content</h2>
        <div className="cards-container">
        <gradio-lite style={{display:"none"}} entrypoint shared-worker>import gradio as gr</gradio-lite>
        {filesContent.map((file, index) => (
          <div key={index} className="card">
            <h3>{file.fileName}</h3>
            <gradio-lite shared-worker>{file.content}</gradio-lite>
          </div>
        ))}
        </div>
      </div>
    </div>
  );
}

export default App;
//todo https://www.gradio.app/custom-components/gallery
//https://huggingface.co/spaces/enzostvs/zero-gpu-spaces
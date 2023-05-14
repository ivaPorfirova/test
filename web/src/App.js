/*global chrome*/
import React from 'react';
import axios from 'axios';
import './App.css';
import {Button} from 'antd';

function App() {
  const [file, setFile] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleFileUpload = () => {
    if (!file) ()
      alert('Please select a file to upload.');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    axios.post('/api/upload_file', formData)
      .then((response) => {
        console.log(response.data);
        alert('File uploaded successfully!');
      })
      .catch((error) => {
        console.error(error);
        alert('File upload failed. Please try again.')
      });
  };

  const handleFileDownload = () => {
    axios.post('/api/download_file', { user_id: 'user1' }, { responseType: 'blob' })
      .then((response) => {
        const url = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', 'file.txt');
        document.body.appendChild(link);
        link.click();
      })
      .catch((error) => {
        console.error(error);
        alert('File download failed. Please try again.');
      });
  }; 

  return (
    <div className='App'>
      <header className='App-header'>
        <img src={logo} className='App-logo' alt='logo' />
        <p> JobHuntPro </p>
        <a
          className='App-link'
          href='https://developer.chrome.com/docs/extensions/mv3/getstarted/'
          target='_blank'
          rel='noopener noreferrer'
        >
          View Extension Dev Docs
        </a>
        <div>
          <input type='file' onChange={handleFileChange} />
          <Button onClick={handleFileUpload}>Upload</Button>
          <Button onClick={handleFileDownload}>Download</Button>
        </div>
      </header>
    </div>
  );
}

export default App;

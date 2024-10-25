import React, { useState } from 'react';
import axios from 'axios';
import './ResumeUpload.css';
import nusLogo from './nus-iss-logo.png';

function ResumeUpload() {
  const [uploadedFiles, setUploadedFiles] = useState([]);
  const [waitingFiles, setWaitingFiles] = useState([]);
  const [dragActive, setDragActive] = useState(false);

  const handleFiles = (files) => {
    const fileArray = Array.from(files);
    const validFiles = fileArray.filter(file =>
      file.type === 'application/pdf' || 
      file.type === 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    );
    setWaitingFiles(validFiles);
  };

  const handleFileSelect = (e) => {
    handleFiles(e.target.files);
  };

  const handleDragEnter = (e) => {
    e.preventDefault();
    setDragActive(true);
  };

  const handleDragLeave = (e) => {
    e.preventDefault();
    setDragActive(false);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    setDragActive(false);
    if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
      handleFiles(e.dataTransfer.files);
    }
  };

  const handleUpload = async () => {
    if (waitingFiles.length === 0) {
      alert("Please upload a file first.");
      return;
    }

    const formData = new FormData();
    waitingFiles.forEach(file => formData.append("resume", file));

    try {
      const response = await axios.post("http://127.0.0.1:7766/api/bulk_upload", formData);
      const data = response.data;
      
      if (data.message === "Recognised" && data.result) {
        // Store the received data in localStorage
        localStorage.setItem('classificationResults', JSON.stringify(data.result));
        window.location.href = "/classification-results";
      } else {
        alert("Upload failed. Please try again.");
      }
    } catch (error) {
      alert("Upload failed. Please check your network or try again.");
    }

    setWaitingFiles([]);
  };

  const handleClear = () => {
    setUploadedFiles([]);
    setWaitingFiles([]);
  };

  return (
    <div className="resume-upload-container">
      <img src={nusLogo} alt="NUS Logo" className="nus-logo" />
      <h2>Resume Upload</h2>
      <div
        className={`upload-area ${dragActive ? 'drag-active' : ''}`}
        onDragEnter={handleDragEnter}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
        onDragOver={(e) => e.preventDefault()}
      >
        <p>{waitingFiles.length > 0 ? "Files selected, click to upload" : "Awaiting file upload"}</p>
        <input
          type="file"
          id="fileInput"
          multiple
          onChange={handleFileSelect}
          accept=".pdf, .doc, .docx"
          style={{ display: 'none' }}
        />
        <label htmlFor="fileInput" className="upload-button">
          Choose Files
        </label>
      </div>

      {waitingFiles.length > 0 && (
        <div className="waiting-files">
          <h3>Files Pending Upload:</h3>
          <ul>
            {waitingFiles.map((file, index) => (
              <li key={index}>
                {file.name} ({(file.size / 1024).toFixed(2)} KB)
              </li>
            ))}
          </ul>
        </div>
      )}

      <div className="buttons">
        <button className="upload-btn" onClick={handleUpload}>Upload</button>
        <button className="clear-btn" onClick={handleClear}>Clear</button>
      </div>
    </div>
  );
}

export default ResumeUpload;


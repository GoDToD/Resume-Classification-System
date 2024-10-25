// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import ResumeUpload from './ResumeUpload';
import ClassificationResults from './ClassificationResults';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<ResumeUpload />} />
        <Route path="/classification-results" element={<ClassificationResults />} />
      </Routes>
    </Router>
  );
}

export default App;




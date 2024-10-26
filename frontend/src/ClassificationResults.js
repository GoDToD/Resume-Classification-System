import React, { useEffect, useState } from 'react';
import './ClassificationResults.css';

function ClassificationResults() {
  const [results, setResults] = useState([]);
  const [expanded, setExpanded] = useState({});

  useEffect(() => {
    const storedResults = localStorage.getItem('classificationResults');
    if (storedResults) {
      setResults(JSON.parse(storedResults));
    } else {
      alert("No classification results found.");
    }
  }, []);

  const mergeResults = (data) => {
    const merged = {};

    data.forEach(detail => {
      const { job_title } = detail;
      if (!merged[job_title]) {
        merged[job_title] = [];
      }
      merged[job_title].push(detail);
    });

    return Object.keys(merged).map(job_title => ({
      job_title,
      details: merged[job_title]
    }));
  };

  const mergedResults = mergeResults(results);

  const toggleExpand = (job_title) => {
    setExpanded((prev) => ({
      ...prev,
      [job_title]: !prev[job_title],
    }));
  };

  return (
    <div className="classification-results-container">
      <h2 className="title">Classification Results</h2>
      {mergedResults.length > 0 ? (
        <div className="results-grid">
          {mergedResults.map((jobResult, index) => (
            <div key={index} className="result-card">
              <h3 className="file-title" onClick={() => toggleExpand(jobResult.job_title)}>
                Job Title: {jobResult.job_title} ({jobResult.details.length})
                {expanded[jobResult.job_title] ? ' ▼' : ' ▲'}
              </h3>
              {expanded[jobResult.job_title] && (
                <div className="result-details">
                  {jobResult.details.map((detail, idx) => (
                    <div key={idx} className="result-detail">
                      <p><strong>Name:</strong> {detail.name || 'N/A'}</p>
                      <p><strong>Email:</strong> <a href={`mailto:${detail.email}`}>{detail.email || 'N/A'}</a></p>
                      <p><strong>Phone:</strong> <a href={`tel:${detail.phone}`}>{detail.phone || 'N/A'}</a></p>
                      {idx < jobResult.details.length - 1 && <hr className="divider" />}
                    </div>
                  ))}
                </div>
              )}
            </div>
          ))}
        </div>
      ) : (
        <p className="no-results">No results available.</p>
      )}
    </div>
  );
}

export default ClassificationResults;

# Resume Classification System Frontend

A React-based user interface for the Resume Classification System, designed to handle resume uploads and display classification results in a structured, user-friendly format. This application is part of a larger system aimed at assisting HR professionals and job-seekers.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Component Overview](#component-overview)
- [API Endpoints](#api-endpoints)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)

## Project Overview
The frontend component of the Resume Classification System offers a smooth interface for résumé upload and classification results viewing. Developed with React, it enables users to upload PDFs and .docx files, which are then processed by the backend to provide classification insights.

## Features
- **Drag-and-Drop File Upload:** Upload résumés quickly via drag-and-drop or file selection.
- **File Validation:** Accepts only PDF and .docx formats.
- **Classification Results:** Displays résumé classification grouped by job title.
- **Responsive Design:** Optimized for various screen sizes.

## Technology Stack
- **Frontend:** React.js
- **HTTP Client:** Axios for API communication
- **State Management:** React hooks (e.g., useState, useEffect)
- **Styling:** Modular CSS

## Installation

### Prerequisites
- **Node.js:** Version 14 or higher
- **NPM:** Package manager (included with Node.js)
- **Backend API:** Ensure backend is available at [http://127.0.0.1:7766](http://127.0.0.1:7766)

### Steps
1. Clone the repository and navigate to the frontend directory:
    ```bash
    git clone https://github.com/GoDToD/Resume-Classification-System.git
    cd Resume-Classification-System/SystemCode/frontend
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Start the development server:
    ```bash
    npm start
    ```
4. Access the app at [http://localhost:3000](http://localhost:3000).

## Usage
- **Upload Files:** Drag and drop files or use the "Choose Files" button.
- **Submit:** Click "Upload" to send files for classification.
- **View Results:** Results are accessible on the classification results page, grouped by job title.

## Component Overview

### 1. ResumeUpload
This component provides the interface for uploading resumes. Key functionalities include:
- **File Selection:** Users can either drag-and-drop files into the upload area or select them manually. Only PDF and .docx formats are accepted.
- **File Validation:** Ensures only valid file types are uploaded, displaying a list of pending files.
- **Bulk Upload:** When the upload button is clicked, files are sent to the backend API endpoint `/api/bulk_upload`.
- **Local Storage:** Upon successful upload, classification results are stored in localStorage, and the user is redirected to the results page.

### 2. ClassificationResults
This component displays the classification results retrieved from localStorage. Key features include:
- **Data Grouping:** Résumés are grouped by job title, and each group shows detailed information such as name, email, phone, gender, and keywords.
- **Expandable Sections:** Users can expand or collapse each job title section to view more or less information as needed.
- **Keyword Relevance:** Keywords are sorted by relevance score, giving a clear view of key skills and their importance.

## API Endpoints
- **Bulk Upload Endpoint:** 
  - **POST:** [http://127.0.0.1:7766/api/bulk_upload](http://127.0.0.1:7766/api/bulk_upload)
  - **Request:** FormData with uploaded résumé files
  - **Response:** JSON containing success message and classification data

## Future Enhancements
- **Advanced Filtering:** Enable filtering of results by skill or experience.
- **Data Visualizations:** Add charts or graphs to better analyze résumé data.

## Contributing
1. Fork the repository.
2. Create a new branch: 
    ```bash
    git checkout -b feature-name
    ```
3. Commit changes: 
    ```bash
    git commit -m 'Add feature'
    ```
4. Push to the branch: 
    ```bash
    git push origin feature-name
    ```
5. Submit a pull request.

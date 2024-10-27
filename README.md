### [ Practice Module ] Project Submission Template: Github Repository & Zip File

**[ Naming Convention ]** CourseCode-StartDate-BatchCode-TeamName-ProjectName.zip

* **[ MTech Thru-Train Group Project Naming Example ]** IRS-PM-2020-01-18-IS02PT-GRP-AwsomeSG-HDB_BTO_Recommender.zip

* **[ MTech Stackable Group Project Naming Example ]** IRS-PM-2020-01-18-STK02-GRP-AwsomeSG-HDB_BTO_Recommender.zip

[Online editor for this README.md markdown file](https://pandao.github.io/editor.md/en.html "pandao")

---

## SECTION 1 : PROJECT TITLE
## IntelliResume Classification and Job Recommendation System 

<img src="Resume.png"
     style="float: left; margin-right: 0px;" />
<img src="result.png"
     style="float: left; margin-right: 0px;" />


---

## SECTION 2 : EXECUTIVE SUMMARY / PAPER ABSTRACT
In today’s competitive job market, effectively matching candidates with the right job roles has become a critical yet challenging task for both job seekers and recruiters. Young professionals often struggle to find positions that align with their skills and career goals, leading to frustration and missed opportunities. Meanwhile, recruiters are faced with the tedious task of sifting through numerous resumes to identify top candidates, which can be both time-consuming and error-prone. Recognizing these challenges, our team of four aspiring professionals aimed to develop an AI-powered "Resume Classification and Recommendation System." This system is designed to improve resume screening efficiency for recruiters while providing job seekers with personalized recommendations to enhance their job search experience.

Our approach to building this system involved a comprehensive understanding of both job seekers' needs and recruiters' requirements. Through surveys and interviews, we gathered insights that informed the creation of a knowledge base for our recommendation engine. On the technical side, we used Java to scrape and compile job data from various online sources, creating a robust database of roles and skill requirements. For the recommendation engine, we utilized CLIPS for rule-based reasoning and combined it with natural language processing (NLP) for resume parsing and skills extraction. Python and React were then used to develop an accessible and user-friendly interface, hosted on a web platform, allowing users to interact seamlessly with the system.

The Resume Recognition and Recommendation System includes advanced features to optimize both the recruitment and job search process. Through NLP and machine learning models, such as BERT, the system parses resumes to identify key skills and experiences, categorizing them by industry relevance. Using the K-Nearest Neighbor (KNN) algorithm, it then matches these skills with job requirements, providing users with tailored job recommendations and relevance scores. Additionally, the system offers job seekers personalized feedback on their resumes and suggestions for skill improvement, equipping them with the insights needed to refine their job search strategy.


Working on this project has been a highly rewarding experience for our team, providing us with practical insights into the recruitment field and the potential of AI-driven solutions. We believe that our system not only addresses the current needs of job seekers and recruiters but also has significant potential for future expansion. In the long term, we envision enhancing the system with additional features, such as location preferences and salary expectations, to provide a more holistic job search experience. Our Resume Recognition and Recommendation System aims to bridge the knowledge gap in job matching, empowering users to make informed career choices while improving recruitment efficiency.

---

## SECTION 3 : CREDITS / PROJECT CONTRIBUTION

| Official Full Name  | Student ID (MTech Applicable)  | Work Items (Who Did What) | Email (Optional) |
| :------------ |:---------------:| :-----| :-----|
| Cheng Siyuan | A0287262X | software structure design, backend development, model deployment, backend data pre-processing and post-processing| e1285208@u.nus.edu |
| Qin Jiayu | A0296744M | Designed the system module, drew the system architecture diagram, wrote the team project report, and searched for data sets| e1350882@u.nus.edu|
| Wang Xiang | A0298765A | xxxxxxxxxx yyyyyyyyyy zzzzzzzzzz| e1352903@u.nus.edu |
| Zhu Yinge | A0295228W | xxxxxxxxxx yyyyyyyyyy zzzzzzzzzz| e1349366@u.nus.edu |

---

## SECTION 4 : VIDEO OF SYSTEM MODELLING & USE CASE DEMO

[![Sudoku AI Solver](http://img.youtube.com/vi/-AiYLUjP6o8/0.jpg)](https://youtu.be/-AiYLUjP6o8 "Sudoku AI Solver")

Note: It is not mandatory for every project member to appear in video presentation; Presentation by one project member is acceptable. 
More reference video presentations [here](https://telescopeuser.wordpress.com/2018/03/31/master-of-technology-solution-know-how-video-index-2/ "video presentations")

---

## SECTION 5 : USER GUIDE

`Refer to appendix <Installation & User Guide> in project report at Github Folder: ProjectReport`

Here's a sample format for a **User Guide** in Markdown format that you could use in your GitHub repository to explain the usage of the frontend and backend:

---

# Resume Recognition and Recommendation System User Guide

This user guide provides instructions on how to set up, run, and interact with the frontend and backend components of the Resume Recognition and Recommendation System.

---

## Table of Contents
1. [System Requirements](#system-requirements)
2. [Backend Setup](#backend-setup)
3. [Frontend Setup](#frontend-setup)
4. [Running the System](#running-the-system)
5. [Using the System](#using-the-system)

---

## System Requirements

Before setting up the system, ensure that you have the following software installed:

- **Python 3.8+**
- **Node.js 14+**
- **npm** (comes with Node.js)
- **Pipenv** (for managing Python dependencies)

---

## Backend Setup

The backend is responsible for processing resumes, classifying skills, and generating job recommendations.

### Step 1: Clone the Repository

```bash
git clone https://github.com/GoDToD/Resume-Classification-System.git
cd Resume-Classification-System/SystemCode
```

### Step 2: Install Dependencies

Navigate to the backend directory and install dependencies using Pipenv:

```bash
cd backend
pipenv install
```

### Step 3: Start the Backend Server

After installing dependencies, you can run the backend server:

```bash
pipenv run python main.py
```

The backend will start on `http://localhost:5000` by default.

---

## Frontend Setup

The frontend provides a user-friendly interface for uploading resumes and viewing job recommendations.

### Step 1: Navigate to the Frontend Directory

```bash
cd ../frontend
```

### Step 2: Install Dependencies

Install the required frontend dependencies using npm:

```bash
npm install
```

### Step 3: Start the Frontend Server

Run the following command to start the frontend server:

```bash
npm start
```

The frontend will start on `http://localhost:3000` by default.

---

## Running the System

Once both frontend and backend servers are running, the system is ready for use. Open your web browser and go to `http://localhost:3000` to access the frontend interface.

---

## Using the System

1. **Upload Resume**: On the main page, upload a resume file in PDF or Word format.
2. **View Analysis**: Once uploaded, the system will analyze the resume and display key skills, experiences, and any extracted information.
3. **Get Job Recommendations**: Based on the extracted data, the system will recommend job positions that match the candidate's profile.
4. **Download Feedback**: Download the generated report with personalized feedback and recommendations.

---

## Troubleshooting

- **Backend not starting**: Ensure you have installed all dependencies and are using Python 3.8 or above.
- **Frontend not displaying**: Verify that all npm dependencies are installed, and the backend is running on the correct port.
- **Connection issues**: Ensure both frontend and backend are running locally on the specified ports (default: 3000 for frontend, 5000 for backend).

---

Feel free to reach out with any questions or issues in the **Issues** section of this repository. Happy coding!
## SECTION 6 : PROJECT REPORT / PAPER

`Refer to project report at Github Folder: ProjectReport`

**Recommended Sections for Project Report / Paper:**
- Executive Summary / Paper Abstract
- Sponsor Company Introduction (if applicable)
- Business Problem Background
- Market Research
- Project Objectives & Success Measurements
- Project Solution (To detail domain modelling & system design.)
- Project Implementation (To detail system development & testing approach.)
- Project Performance & Validation (To prove project objectives are met.)
- Project Conclusions: Findings & Recommendation
- Appendix of report: Project Proposal
- Appendix of report: Mapped System Functionalities against knowledge, techniques and skills of modular courses: MR, RS, CGS
- Appendix of report: Installation and User Guide
- Appendix of report: 1-2 pages individual project report per project member, including: Individual reflection of project journey: (1) personal contribution to group project (2) what learnt is most useful for you (3) how you can apply the knowledge and skills in other situations or your workplaces
- Appendix of report: List of Abbreviations (if applicable)
- Appendix of report: References (if applicable)

---
## SECTION 7 : MISCELLANEOUS

`Refer to Github Folder: Miscellaneous`

### HDB_BTO_SURVEY.xlsx
* Results of survey
* Insights derived, which were subsequently used in our system

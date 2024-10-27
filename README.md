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
In today’s competitive job market, effectively matching candidates with the right job roles has become a critical yet challenging task for both job seekers and recruiters. Young professionals often struggle to find positions that align with their skills and career goals, leading to frustration and missed opportunities. Meanwhile, recruiters are faced with the tedious task of sifting through numerous resumes to identify top candidates, which can be both time-consuming and error-prone. Recognizing these challenges, our team of six aspiring professionals aimed to develop an AI-powered "Resume Recognition and Recommendation System." This system is designed to improve resume screening efficiency for recruiters while providing job seekers with personalized recommendations to enhance their job search experience.

Our approach to building this system involved a comprehensive understanding of both job seekers' needs and recruiters' requirements. Through surveys and interviews, we gathered insights that informed the creation of a knowledge base for our recommendation engine. On the technical side, we used Java to scrape and compile job data from various online sources, creating a robust database of roles and skill requirements. For the recommendation engine, we utilized CLIPS for rule-based reasoning and combined it with natural language processing (NLP) for resume parsing and skills extraction. Python and React were then used to develop an accessible and user-friendly interface, hosted on a web platform, allowing users to interact seamlessly with the system.

The Resume Recognition and Recommendation System includes advanced features to optimize both the recruitment and job search process. Through NLP and machine learning models, such as BERT, the system parses resumes to identify key skills and experiences, categorizing them by industry relevance. Using the K-Nearest Neighbor (KNN) algorithm, it then matches these skills with job requirements, providing users with tailored job recommendations and relevance scores. Additionally, the system offers job seekers personalized feedback on their resumes and suggestions for skill improvement, equipping them with the insights needed to refine their job search strategy.


Working on this project has been a highly rewarding experience for our team, providing us with practical insights into the recruitment field and the potential of AI-driven solutions. We believe that our system not only addresses the current needs of job seekers and recruiters but also has significant potential for future expansion. In the long term, we envision enhancing the system with additional features, such as location preferences and salary expectations, to provide a more holistic job search experience. Our Resume Recognition and Recommendation System aims to bridge the knowledge gap in job matching, empowering users to make informed career choices while improving recruitment efficiency.

---

## SECTION 3 : CREDITS / PROJECT CONTRIBUTION

| Official Full Name  | Student ID (MTech Applicable)  | Work Items (Who Did What) | Email (Optional) |
| :------------ |:---------------:| :-----| :-----|
| Cheng Siyuan | A0287262X | software structure design, backend development, model deployment, backend data pre-processing and post-processing| e1285208@u.nus.edu |
| Qin Jiayu | A1234567B | xxxxxxxxxx yyyyyyyyyy zzzzzzzzzz| A1234567B@gmail.com |
| Wang Xiang | A1234567C | xxxxxxxxxx yyyyyyyyyy zzzzzzzzzz| A1234567C@outlook.com |
| Zhu Yinge | A1234567D | xxxxxxxxxx yyyyyyyyyy zzzzzzzzzz| A1234567D@yahoo.com |

---

## SECTION 4 : VIDEO OF SYSTEM MODELLING & USE CASE DEMO

[![Sudoku AI Solver](http://img.youtube.com/vi/-AiYLUjP6o8/0.jpg)](https://youtu.be/-AiYLUjP6o8 "Sudoku AI Solver")

Note: It is not mandatory for every project member to appear in video presentation; Presentation by one project member is acceptable. 
More reference video presentations [here](https://telescopeuser.wordpress.com/2018/03/31/master-of-technology-solution-know-how-video-index-2/ "video presentations")

---

## SECTION 5 : USER GUIDE

`Refer to appendix <Installation & User Guide> in project report at Github Folder: ProjectReport`

### [ 1 ] To run the system using iss-vm

> download pre-built virtual machine from http://bit.ly/iss-vm

> start iss-vm

> open terminal in iss-vm

> $ git clone https://github.com/telescopeuser/Workshop-Project-Submission-Template.git

> $ source activate iss-env-py2

> (iss-env-py2) $ cd Workshop-Project-Submission-Template/SystemCode/clips

> (iss-env-py2) $ python app.py

> **Go to URL using web browser** http://0.0.0.0:5000 or http://127.0.0.1:5000

### [ 2 ] To run the system in other/local machine:
### Install additional necessary libraries. This application works in python 2 only.

> $ sudo apt-get install python-clips clips build-essential libssl-dev libffi-dev python-dev python-pip

> $ pip install pyclips flask flask-socketio eventlet simplejson pandas

---
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

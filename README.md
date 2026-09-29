# 🤖 AI Recruiter — Resume Screening System

An AI-powered resume screening and candidate-job matching system built with Python and Streamlit.

The application allows recruiters to paste a Job Description (JD), upload multiple candidate resumes, and automatically analyze how closely each candidate matches the role.

It uses AI to evaluate resumes based on job-related skills, experience, education, projects, and overall relevance to the provided job description.

---

## 🚀 Features

### 📋 Job Description Analysis
- Paste a complete Job Description into the application.
- The JD is used as the basis for evaluating every candidate.

### 📄 Multiple Resume Upload
- Upload multiple candidate resumes in PDF format.
- Automatically extracts resume text using `pdfplumber`.

### 🤖 AI-Powered Resume Screening
- Uses the OpenAI API to analyze resumes against the JD.
- Generates structured candidate analysis.
- Provides job-related matching scores.

### 📊 Candidate Scoring

Each candidate receives scores for:

- Overall Match
- Skill Match
- Experience Match
- Education Match
- Project Match
- JD Relevance

### 🏆 Candidate Ranking
- Candidates are automatically ranked according to their overall match score.
- Recruiters can quickly compare multiple candidates.

### ✅ Matched Skills
Identifies skills present in the resume that are relevant to the job description.

### ⚠️ Missing / Weak Skills
Identifies important skills from the JD that are missing or not clearly demonstrated in the resume.

### 💼 Experience Analysis
Provides a summary of the candidate's relevant experience.

### 🎓 Education Analysis
Evaluates the relevance of the candidate's educational background.

### 🛠️ Project Analysis
Identifies projects that are relevant to the job requirements.

### 💪 Strengths & Gaps
Provides recruiter-friendly information about:

- Candidate strengths
- Job-related gaps
- Relevant technical skills
- Practical project experience

### 🧑‍💼 Recruiter Summary
Generates a concise summary that helps recruiters understand the candidate's relevance to the role.

### 🔄 Fallback Matching
If AI analysis is temporarily unavailable, the application can use local keyword-based matching to provide a preliminary resume-JD match instead of returning meaningless results.

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **OpenAI API**
- **pdfplumber**
- **python-dotenv**
- **Regular Expressions (Regex)**
- **Git & GitHub**

---

## 🏗️ Application Workflow

```text
                 Job Description
                        │
                        ▼
                ┌───────────────┐
                │  AI Recruiter │
                └───────────────┘
                        │
          ┌─────────────┴─────────────┐
          │                           │
          ▼                           ▼
   Candidate Resume 1         Candidate Resume 2
          │                           │
          └─────────────┬─────────────┘
                        │
                        ▼
                PDF Text Extraction
                        │
                        ▼
                 Resume Analysis
                        │
                        ▼
              JD ↔ Resume Matching
                        │
                        ▼
              ┌───────────────────┐
              │ Candidate Scoring │
              └───────────────────┘
                        │
                        ▼
                 Candidate Ranking
                        │
                        ▼
        ┌──────────────────────────────┐
        │ Matched Skills               │
        │ Missing Skills               │
        │ Experience                   │
        │ Education                   │
        │ Projects                    │
        │ Strengths & Gaps             │
        │ Recruiter Summary            │
        └──────────────────────────────┘

import streamlit as st
import pdfplumber
from openai import OpenAI

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# ---------------- STYLING ----------------
st.markdown("""
<style>
.skill-box {
    display: inline-block;
    padding: 8px 12px;
    margin: 5px;
    border-radius: 10px;
    background-color: #1f77b4;
    color: white;
    font-size: 14px;
}
.missing-box {
    display: inline-block;
    padding: 8px 12px;
    margin: 5px;
    border-radius: 10px;
    background-color: #ff4b4b;
    color: white;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- OPENAI ----------------
# 🔴 Replace with your real API key
client = OpenAI(api_key="YOUR_API_KEY")

# ---------------- ROLE DATABASE ----------------
roles = {
    "Software Engineer": ["python", "c++", "java", "sql", "data structures", "algorithms"],
    "Data Scientist": ["python", "machine learning", "statistics", "pandas", "numpy", "sql"],
    "Web Developer": ["html", "css", "javascript", "react", "node", "mongodb"]
}

# ---------------- UI ----------------
st.title("🚀 AI Resume Analyzer")
st.caption("Analyze your resume, match roles, and get AI-powered suggestions")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

# ---------------- FUNCTIONS ----------------
def extract_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def extract_skills(text):
    skills_db = ["python", "java", "c++", "sql", "machine learning", "react", "html", "css", "javascript"]
    found_skills = []
    for skill in skills_db:
        if skill in text.lower():
            found_skills.append(skill)
    return found_skills

def match_role(skills):
    best_role = None
    max_match = 0
    missing_skills = []

    for role, role_skills in roles.items():
        match_count = len(set(skills) & set(role_skills))

        if match_count > max_match:
            max_match = match_count
            best_role = role
            missing_skills = list(set(role_skills) - set(skills))

    return best_role, missing_skills

def calculate_ats_score(skills, role_skills):
    match = len(set(skills) & set(role_skills))
    total = len(role_skills)
    return int((match / total) * 100)

def get_ai_suggestions(skills, role):
    prompt = f"""
    I have these skills: {skills}.
    I want to become a {role}.

    Suggest:
    - Missing skills
    - Resume improvements
    - 2 project ideas
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

# ---------------- MAIN LOGIC ----------------
if uploaded_file:
    text = extract_text(uploaded_file)
    skills = extract_skills(text)

    # -------- Skills Display --------
    st.subheader("✅ Extracted Skills")
    for skill in skills:
        st.markdown(f'<span class="skill-box">{skill}</span>', unsafe_allow_html=True)

    # -------- Role Matching --------
    role, missing = match_role(skills)

    # -------- ATS Score --------
    role_skills = roles[role]
    ats_score = calculate_ats_score(skills, role_skills)

    # -------- Layout --------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🎯 Best Role")
        st.success(role)

    with col2:
        st.subheader("📊 ATS Score")
        st.progress(ats_score)
        st.write(f"{ats_score}% match")

    # -------- Missing Skills --------
    st.subheader("⚠️ Missing Skills")
    for skill in missing:
        st.markdown(f'<span class="missing-box">{skill}</span>', unsafe_allow_html=True)

    # -------- AI Suggestions --------
    st.subheader("🤖 AI Suggestions")

    if st.button("Get AI Suggestions"):
        with st.spinner("Analyzing with AI... 🤖"):
            result = get_ai_suggestions(skills, role)

        st.success("Analysis Complete!")

        with st.expander("Click to view suggestions"):
            st.write(result)
import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
import json
from dotenv import load_dotenv
import re

# Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to clean the JSON response
def clean_json_response(response_text):
    """Clean the JSON response to ensure it can be properly parsed."""
    # Remove any markdown code block indicators
    response_text = re.sub(r'```json|```', '', response_text).strip()
    
    # Try to extract just the JSON part if there's text before or after
    json_match = re.search(r'(\{.*\})', response_text, re.DOTALL)
    if json_match:
        response_text = json_match.group(1)
        
    return response_text

# Function to get response from Gemini
def get_gemini_response(input_prompt):
    try:
        model = genai.GenerativeModel('gemini-1.5-pro')  # Ensure correct model name
        # Add instructions to return valid JSON without markdown formatting
        enhanced_prompt = f"{input_prompt}\n\nIMPORTANT: Return your response as valid JSON without any markdown formatting. Do not use asterisks, quotation marks, or other markdown syntax in the content of the JSON values."
        response = model.generate_content(enhanced_prompt)
        return response.text if response else "Error: No response received from AI."
    except Exception as e:
        return f"Error: {str(e)}"  # Handle API errors gracefully

# Function to extract text from uploaded PDF
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() if page.extract_text() else ""  # Avoid NoneType errors
    return text

# Streamlit App Styling
st.set_page_config(page_title="Smart ATS Resume Evaluator", page_icon="🔍")

# Custom CSS
st.markdown(
    """
    <style>
    .main {
        padding: 2rem;
    }
    h1 {
        color: #2c3e50;
        margin-bottom: 20px;
    }
    h2 {
        color: #3498db;
        margin-top: 30px;
        margin-bottom: 15px;
        padding-bottom: 10px;
        border-bottom: 1px solid #eee;
    }
    h3 {
        color: #34495e;
        margin-top: 20px;
        margin-bottom: 15px;
    }
    ul {
        list-style: disc;
        padding-left: 20px;
    }
    ul li {
        background: #ecf0f1;
        margin: 8px 0;
        padding: 12px 15px;
        border-radius: 5px;
        font-size: 16px;
    }
    strong {
        color: #27ae60;
    }
    .error {
        color: #e74c3c;
        font-weight: bold;
    }
    .match-score {
        font-size: 18px;
        padding: 15px;
        background-color: #f8f9fa;
        border-radius: 8px;
        border-left: 5px solid #27ae60;
        margin-bottom: 20px;
    }
    .missing-keywords {
        margin-top: 25px;
        margin-bottom: 25px;
    }
    .keyword-item {
        background-color: #f1f8e9;
        border-left: 3px solid #8bc34a;
        padding: 10px 15px;
        margin: 8px 0;
        border-radius: 4px;
        font-size: 15px;
    }
    .suggestion-item {
        background-color: #e3f2fd;
        border-left: 3px solid #2196f3;
        padding: 12px 15px;
        margin: 10px 0;
        border-radius: 4px;
        font-size: 15px;
        line-height: 1.5;
    }
    .divider {
        height: 1px;
        background-color: #e0e0e0;
        margin: 30px 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Streamlit App
st.title("🔍 Smart ATS Resume Evaluator")
st.write("**Optimize Your Resume for ATS & Get Expert Insights**")

# Input Fields
jd = st.text_area("📌 Paste the Job Description")
uploaded_file = st.file_uploader("📄 Upload Your Resume (PDF)", type="pdf", help="Upload a PDF resume for analysis.")

submit = st.button("🚀 Analyze Resume")

if submit:
    if uploaded_file is not None and jd.strip() != "":
        resume_text = input_pdf_text(uploaded_file)

        # Sample Prompt (Update with Full JSON Structure if Needed)
        input_prompt = f"""
        Analyze the following resume against this job description and provide ATS insights.

        Resume: {resume_text}
        Job Description: {jd}

        Provide your analysis in the following JSON format:
        {{
            "JD Match": "Strong/Medium/Low", // Provide a qualitative assessment with a detailed explanation
            "MissingKeywords": ["keyword1", "keyword2", ...], // List complete keywords, not individual letters
            "Resume Suggestions": [
                "Suggestion 1 without any markdown formatting or special characters",
                "Suggestion 2 without any markdown formatting or special characters",
                ...
            ]
        }}

        IMPORTANT: 
        1. Return your response as valid JSON without any markdown formatting.
        2. Do not use asterisks, quotation marks, or other markdown syntax in the content of the JSON values.
        3. For MissingKeywords, provide complete words/phrases, not individual letters.
        4. Ensure each suggestion is clear, actionable, and free of formatting characters.
        """

        # Get AI Response
        response = get_gemini_response(input_prompt)

        # Display Results
        st.subheader("📊 ATS Evaluation Results")
        try:
            # Clean the response before parsing
            cleaned_response = clean_json_response(response)
            ats_result = json.loads(cleaned_response)  # Ensure valid JSON parsing

            # Display JD Match Percentage
            jd_match = ats_result.get('JD Match', 'Unknown')
            st.markdown(f"""
            <div class="match-score">
                <h2>🎯 JD Match: {jd_match}</h2>
            </div>
            """, unsafe_allow_html=True)

            # Display Missing Keywords (if any)
            missing_keywords = ats_result.get("MissingKeywords", [])
            if missing_keywords:
                st.markdown('<div class="missing-keywords">', unsafe_allow_html=True)
                st.markdown("### 🔍 Missing Keywords")
                st.write("These essential keywords are missing from the resume:")
                
                # Create a formatted list of keywords
                keywords_html = ""
                for keyword in missing_keywords:
                    keywords_html += f'<div class="keyword-item">{keyword}</div>'
                
                st.markdown(keywords_html, unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Add a divider
                st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

            # Display Resume Suggestions
            resume_suggestions = ats_result.get("Resume Suggestions", [])
            if resume_suggestions:
                st.markdown("### 📌 Resume Improvement Suggestions")
                
                # Create formatted suggestions
                suggestions_html = ""
                for i, suggestion in enumerate(resume_suggestions):
                    # Remove asterisks and quotation marks from the suggestion text
                    clean_suggestion = suggestion.replace('**', '').replace('"', '')
                    suggestions_html += f'<div class="suggestion-item">{i+1}. {clean_suggestion}</div>'
                
                st.markdown(suggestions_html, unsafe_allow_html=True)

        except json.JSONDecodeError:
            st.error("❌ AI Response Error: Invalid JSON format.")
            st.markdown("""
            <div style="background-color: #ffebee; padding: 15px; border-radius: 5px; border-left: 5px solid #f44336;">
                <h3 style="color: #d32f2f; margin-top: 0;">Error Processing Results</h3>
                <p>We encountered an issue while processing the AI response. This might be due to:</p>
                <ul style="margin-bottom: 0;">
                    <li>Complex formatting in your resume</li>
                    <li>Unusual characters or symbols</li>
                    <li>Very long or complex job descriptions</li>
                </ul>
                <p style="margin-top: 15px;">Please try again with a simplified resume or job description.</p>
            </div>
            """, unsafe_allow_html=True)
            
            # For debugging purposes, show the raw response in a collapsible section
            with st.expander("Show Technical Details"):
                st.text(response)
    else:
        st.error("⚠️ Please upload a resume and paste the job description before submitting.")

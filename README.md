# 🚀 Smart ATS Resume Evaluator

## 📌 Overview
**Smart ATS Resume Evaluator** is an AI-powered web application that analyzes resumes against job descriptions, identifies missing keywords, and suggests improvements to optimize for **Applicant Tracking Systems (ATS)**. The app also generates a **professionally formatted, ATS-friendly resume PDF** based on AI recommendations.

## 🎯 Features
✅ **AI-Powered Resume Analysis** – Evaluates resume alignment with job descriptions using **Google Gemini AI**.  
✅ **ATS Optimization** – Identifies missing keywords and recommends **improvements** for better ATS ranking.  
✅ **Real-Time Resume Scoring** – Provides a **JD Match Score (Percentage)** to indicate ATS compatibility.  
✅ **Instant Resume Formatting** – Generates a **PDF with improved structure, font, and alignment** for professional appeal.  
✅ **Interactive UI** – Built with **Streamlit** for a clean and seamless user experience.  

## 🛠️ Tech Stack
- **Python** – Core programming language.  
- **Google Gemini AI** – NLP-powered resume analysis.  
- **Streamlit** – Interactive UI for real-time resume analysis.  
- **PyPDF2** – Extracts text from uploaded resumes (PDFs).  
- **ReportLab** – Generates professional **ATS-friendly** resume PDFs.  
- **dotenv** – Manages API keys securely.  

## 🚀 How It Works
1. **Upload Resume** – Upload your **PDF resume** to be analyzed.  
2. **Paste Job Description** – Enter the job description for comparison.  
3. **AI-Powered Evaluation** – The system will:  
   - Provide a **JD Match Percentage** (How well your resume aligns).  
   - Identify **missing keywords** required for ATS optimization.  
   - Offer **improvement suggestions** to make the resume stronger.  
4. **Download Optimized Resume** – Get a **professionally formatted ATS-ready PDF** with AI-powered suggestions applied.  

## 📸 Screenshots
| Upload Resume | AI Evaluation | Download Improved Resume |
|--------------|--------------|-------------------------|
| ![Upload](assets/upload.png) | ![Evaluation](assets/evaluation.png) | ![Download](assets/download.png) |

## 🎯 Why Use This?
- **Boost your ATS ranking** – Ensure your resume passes ATS filters for higher visibility.  
- **Professional Formatting** – Get a **clean, structured, and well-aligned** resume instantly.  
- **Instant Insights** – Save hours by **quickly optimizing your resume** for any job description.  

## 🏗️ Installation & Setup
1️⃣ **Clone the Repository**
```bash
git clone https://github.com/yourusername/smart-ats-resume-evaluator.git
cd smart-ats-resume-evaluator
```

2️⃣ **Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

4️⃣ **Set Up API Keys**
Create a `.env` file and add your **Google Gemini AI API key**:
```bash
GOOGLE_API_KEY=your_api_key_here
```

5️⃣ **Run the Application**
```bash
streamlit run app.py
```

## 👨‍💻 Future Enhancements
🔹 **Custom Resume Templates** – Users can choose from multiple resume templates.  
🔹 **Keyword Density Analysis** – Visualize keyword optimization via **charts**.  
🔹 **AI Cover Letter Generation** – Automatically generate **tailored cover letters**.  
🔹 **Multi-Resume Comparison** – Compare multiple resumes to **choose the strongest version**.  

## 🤝 Contributing
Want to improve **Smart ATS Resume Evaluator**? Feel free to **fork the repo** and submit pull requests. Contributions are always welcome!  

## 📜 License
This project is licensed under the **MIT License**.  

## 🌟 Show Your Support
If you find this project useful, please **⭐ Star this repo** and share it with others who might benefit!  

---  
🔥 **Landing more interviews starts with the right resume – Optimize yours today!**

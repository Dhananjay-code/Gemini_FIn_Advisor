# 🏦 AI Financial Advisor
**A production-ready chatbot focused on conservative wealth building and educational budgeting.**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)
[![Powered by Gemini](https://img.shields.io/badge/AI-Gemini%202.5%20Flash-orange)](https://ai.google.dev/)

---

## 🌟 Overview
This application is a specialized AI Financial Advisor built with **Google Gemini 2.5 Flash**. It provides users with real-time, conservative financial guidance on budgeting, 401k planning, and wealth-building strategies.

### **Key Features**
* **Real-time Streaming:** Smooth "typing" effect using `st.write_stream` for a premium chat experience.
* **Custom UI/UX:** Advanced CSS injection featuring glassmorphism effects and high-visibility typography.
* **State Management:** Session-aware conversations that remember user context during the session.
* **Cloud Hosted:** Fully deployed on **AWS EC2** with optimized port forwarding (80 -> 8501).

---

## 🛠️ Tech Stack
* **LLM:** Google Gemini 2.5 Flash
* **Frontend:** Streamlit (Python-based web framework)
* **Backend logic:** Python `google-genai` SDK
* **Deployment:** AWS EC2 (Ubuntu 24.04 LTS)
* **Environment:** `python-dotenv` for secure API secret management

---

## 🚀 Getting Started

### **Prerequisites**
* Python 3.10 or higher
* A Google Gemini API Key ([Get one here](https://aistudio.google.com/))

### **Local Installation**
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/Gemini_Fin_Advisor.git](https://github.com/your-username/Gemini_Fin_Advisor.git)
   cd Gemini_Fin_Advisor

    Create a virtual environment:
    Bash

    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

    Install dependencies:
    Bash

    pip install -r requirements.txt

    Set up Environment Variables:
    Create a .env file in the root directory and add your API key:
    Code snippet

    GEMINI_API_KEY=your_actual_api_key_here

    Run the App:
    Bash

    streamlit run app.py

🎨 Design Philosophy

The UI was built to prioritize readability and modern aesthetics.

    Background: Dynamic image injection via Base64 encoding.

    Transparency: Fully transparent chat containers to showcase branding.

    Contrast: Heavy text-shadowing implemented via custom CSS to ensure readability across diverse background images.

📜 License

Distributed under the MIT License. See LICENSE for more information.


---

### **Final Pro-Tips for your GitHub:**
* **Add an Image/GIF:** In the `Overview` section, add `![App Demo](demo.gif)`. Seeing the "streaming" text in action significantly increases the "wow" factor for recruiters.
* **The Repository "About" Section:** On the right-hand side of your GitHub repo page, add the description: *"AI Financial Advisor powered by Gemini 2.5 Flash and Streamlit, deployed on AWS EC2."* and add tags like `#python`, `#ai`, `#aws`, and `#fintech`.
* **License File:** Create a file named `LICENSE` and paste the [MIT License text](https://opensource.org/license/mit/) into it. It makes your project feel officially "Open Source."



**You're all set!** Your project is live on AWS, your LinkedIn post is ready to go, and your GitHub is polished. Is there anything else you'd like to tweak before you hit "Post"?

This [Streamlit Chatbot Best Practices](https://www.youtube.com/watch?v=sCqXieMcwDg) video is a great resource for learning about more advanced features like session management and persistent memory that you could add to your advisor in the future.


http://googleusercontent.com/youtube_content/3

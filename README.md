# Excel Cleaner — Pro v1

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://excel-cleaner-pro-v1-xxxxx.streamlit.app)

A polished *Excel cleaning tool* built with *Python + Streamlit*.  
It transforms messy spreadsheets into clean, analysis-ready data in seconds.  

---

## ✨ Key Features
- 🧹 Remove duplicate rows instantly  
- 🔠 Standardize text (trim spaces, fix case, remove symbols)  
- 📅 Parse multiple date formats into one clean format  
- 💰 Clean numeric fields (remove commas, currency signs, standardize)  
- 📊 Handle missing values (drop or fill with defaults)  
- 📥 Download cleaned Excel/CSV file in one click  

---

## 📸 Demo

*Before cleaning*  
![Before](assets/before.png)

*After cleaning*  
![After](assets/after.png)

🎥 [Watch demo video](assets/demo.mp4)

---

## 🚀 Live App
Click below to try it instantly (no install required):  
👉 [Excel Cleaner Pro v1 on Streamlit](https://excel-cleaner-pro-v1-xxxxx.streamlit.app)

---

## 🛠 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/zaidkhan-automation/excel-cleaner-pro-v1.git
cd excel-cleaner-pro-v1

# Create virtual env
python -m venv venv
# Windows
.\venv\Scripts\Activate
# Linux/Mac
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run src/app.py
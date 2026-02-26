# 🛡️ SafeLinker - Fraud Link Detector

Ever received a suspicious link and wondered — *is this safe to click?*  
SafeLinker was built to answer exactly that question.

## 🚀 Live Demo
👉 Try SafeLinker here -(https://renukawagh-safelinker.hf.space)

##  What is SafeLinker?
SafeLinker is a Machine Learning powered web app that analyzes a URL and tells you 
whether it's **safe or a phishing attempt** — in seconds.

It looks at 87 different URL characteristics and uses a trained XGBoost model to make 
that decision with **97% accuracy**.

## 🛠️ Built With
- **Python** — core language
- **XGBoost** — ML model (97% accuracy)
- **Flask** — web framework
- **Bootstrap** — frontend UI
- **Pandas & Scikit-learn** — data processing

## 📊 Behind the Model
- Trained on **11,430 real-world URLs**
- **87 URL-based features** analyzed
- Perfectly balanced dataset — 50% legitimate, 50% phishing

##  Run it Locally
```bash
pip install -r requirements.txt
python server/app.py
```
Then open `http://localhost:8000` in your browser.

## ⚠️ Disclaimer
This project was built for educational purposes.  
Always use caution when visiting unknown links.

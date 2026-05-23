# 🛡️ SafeLinker – Fraud Link Detector

SafeLinker is a Machine Learning based phishing URL detection system that analyzes suspicious links and predicts whether they are **legitimate** or **fraudulent**.

The application extracts URL characteristics, processes them using an ML pipeline, and provides instant prediction results through a web interface.

---

##  Live Demo

 https://renukawagh-safelinker.hf.space

---

##  Project Overview

Phishing attacks commonly use malicious URLs to steal sensitive information. SafeLinker helps identify such URLs by analyzing multiple URL characteristics and using a trained Machine Learning model for prediction.

### Key Features

✔ Detects phishing and malicious URLs  
✔ Real-time prediction system  
✔ Feature extraction from URLs  
✔ Machine Learning based classification  
✔ User-friendly web interface  
✔ Fast prediction response

---

## Technologies Used

- Python
- Flask
- XGBoost
- Pandas
- NumPy
- Scikit-learn
- Bootstrap

---

## 📊 Model Information

- Dataset Size: **11,430 URLs**
- Features Extracted: **87 URL features**
- Dataset Distribution:
  - 50% Legitimate URLs
  - 50% Phishing URLs
- Model Used: **XGBoost Classifier**
- Accuracy Achieved: **97%**

---

## 📂 Project Structure

```bash
fraud-link-detector/
│── app/
│── model/
│── static/
│── templates/
│── feature_extraction.py
│── app.py
│── requirements.txt
│── README.md
```

---

## ⚙ Installation

Clone repository:

```bash
git clone https://github.com/Renukaw2126/fraud-link-detector.git
```

Move into project:

```bash
cd fraud-link-detector
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run application:

```bash
python server/app.py
```

Open browser:

```text
http://localhost:8000
```

---

## Working Process

1. User enters URL  
2. System extracts URL features  
3. Features are processed by XGBoost model  
4. Prediction generated  
5. Result displayed as Safe / Fraudulent

---

## Future Improvements

- Browser extension support
- API integration
- Threat scoring system
- URL history tracking
- Real-time blacklist integration

---

## Author

**Renuka Wagh**

GitHub: https://github.com/Renukaw2126

Project developed for educational and portfolio purposes.

---

##  Disclaimer

This application provides predictive analysis only and does not guarantee complete cybersecurity protection.

Always verify suspicious links manually before opening them.

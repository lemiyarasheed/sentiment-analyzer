---
title: Sentiment Analyzer
emoji: 🎭
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: "1.35.0"
python_version: "3.11"
app_file: app.py
pinned: false
preload_from_hub:
  - j-hartmann/emotion-english-distilroberta-base
---
# 🎭 Emotion & Sentiment Analyzer

A web app that detects **7 emotions** (anger, disgust, fear, joy, neutral, sadness, surprise) from text using a pre-trained Hugging Face transformer model.

## 🚀 Live Demo

[![Open in Spaces](https://img.shields.io/badge/🤗-Open%20in%20Spaces-blue)](https://huggingface.co/spaces/lemiyarasheed/sentiment-analyzer)

## ✨ Features

- 🔍 Real-time emotion detection
- 📊 Confidence score for each prediction
- 📜 Analysis history tracking
- 🎨 Color-coded results (positive emotions in green, negative in red)
- 😊 Emoji icons for each emotion type

## 🛠️ Technologies

- Python 3.11+
- Streamlit (Web interface)
- Hugging Face Transformers
- PyTorch (backend for the model)
- Pandas (data handling)

## 📋 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/lemiyarasheed/sentiment-analyzer.git
cd sentiment-analyzer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
🎭 Emotions Detected
Emotion	Emoji	Color
Joy	😀	Green (positive)
Sadness	😢	Red (negative)
Anger	😤	Red (negative)
Fear	😨	Red (negative)
Disgust	🤢	Red (negative)
Surprise	😲	Neutral
Neutral	😐	Neutral
💬 Example Inputs
Text	Predicted Emotion
"I absolutely love this product!"	joy
"This is terrible, I hate it."	anger
"The sky is blue today."	neutral
"I can't believe I won the lottery!"	surprise
📁 Project Structure
text
sentiment-analyzer/
├── app.py              # Streamlit web application
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── .gitignore         # Excluded files
🧠 Model Information
Model: j-hartmann/emotion-english-distilroberta-base

Architecture: DistilRoBERTa (distilled for speed)

Training data: Combination of 6 emotion datasets

Accuracy: ~66% on emotion classification tasks

🎯 Use Cases
Customer feedback analysis

Social media monitoring

Mental health support tools

Market research

Content moderation

👩‍💻 Author
Lemiya Rasheed
AI & Automation Specialist
GitHub

📅 Status
Version: 1.0
Last updated: April 28, 2026
Status: ✅ Working

🚀 Coming Soon
Add support for longer text (beyond single sentences)

Batch processing for multiple texts

Export analysis results to CSV

Visualization charts for emotion trends
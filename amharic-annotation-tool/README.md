<h1>Amharic POS & NER Human-in-the-Loop Annotation Tool</h1>

<h3>Overview</h3>

This project provides a mouse-based annotation tool for Amharic natural language processing (NLP).
It allows human annotators to tag each word in an Amharic sentence with:

<h3>POS (Part of Speech) tags</h3>
<h3>NER (Named Entity Recognition) tags</h3>

The tool is designed for human-in-the-loop workflows, enabling the creation of high-quality labeled data for low-resource language modeling, evaluation, and retraining.


<h3>Run Instructions</h3>

python -m venv .venv </br>
source .venv/bin/activate   # Windows: .venv\Scripts\activate </br>
pip install -r requirements.txt</br>
streamlit run app.py</br>

<img width="1334" height="612" alt="image" src="https://github.com/user-attachments/assets/553d36e1-6253-40b5-8c9a-5351fba0cd3b" />

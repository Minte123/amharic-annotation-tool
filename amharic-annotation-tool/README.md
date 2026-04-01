<h3>Amharic POS & NER Human-in-the-Loop Annotation Tool<h3>

<h6>Overview<h6>

This project provides a mouse-based annotation tool for Amharic natural language processing (NLP).
It allows human annotators to tag each word in an Amharic sentence with:

<h6>POS (Part of Speech) tags<h6>
<h6>NER (Named Entity Recognition) tags<h6>

The tool is designed for human-in-the-loop workflows, enabling the creation of high-quality labeled data for low-resource language modeling, evaluation, and retraining.


<h3>Run Instructions</h3>

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py


import streamlit as st
from tagsets import POS_TAGS, NER_TAGS
from storage import save_annotation

# Page configuration
st.set_page_config(
    page_title="Amharic POS & NER Annotation Tool",
    layout="wide"
)

st.title("Amharic POS & NER Human Annotation Tool")

# Input sentence
sentence = st.text_input(
    label="Enter an Amharic sentence",
    value="አብይ አህመድ ዛሬ በአዲስ አበባ ንግግር አደረጉ"
)

if sentence.strip():
    tokens = sentence.split()
    annotations = []

    st.subheader("Tag each word")

    for idx, token in enumerate(tokens):
        with st.container():
            col_word, col_pos, col_ner = st.columns([2, 2, 2])

            # Display word (click-target)
            with col_word:
                st.markdown(f"**{token}**")

            # POS selector
            with col_pos:
                pos = st.selectbox(
                    label="POS",
                    options=POS_TAGS,
                    key=f"pos_{idx}"
                )

            # NER selector
            with col_ner:
                ner = st.selectbox(
                    label="NER",
                    options=NER_TAGS,
                    key=f"ner_{idx}"
                )

            annotations.append({
                "word": token,
                "pos": pos,
                "ner": ner
            })

    if st.button("Save Annotation"):
        record = {
            "sentence": sentence,
            "tokens": annotations
        }

        save_annotation(record)
        st.success("Annotation saved successfully.")
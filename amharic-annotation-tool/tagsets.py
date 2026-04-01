# Universal POS tags (simplified)
POS_TAGS = [
    "NOUN", "VERB", "ADJ", "ADV", "PRON",
    "PROPN", "ADP", "AUX", "CCONJ",
    "DET", "NUM", "PART", "SCONJ", "PUNCT"
]

# NER tags (standard IOB-free for simplicity)
NER_TAGS = [
    "PER",     # Person
    "LOC",     # Location
    "ORG",     # Organization
    "DATE",
    "TIME",
    "O"        # Outside / Not an entity
]
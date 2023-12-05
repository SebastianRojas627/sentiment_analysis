import spacy

class TextAnalyzer:
    def __init__(self):
        self.nlp = spacy.load("es_core_news_sm")

    def analyse_text(self, text):
        doc = self.nlp(text)
        pos_tags = [{'token': token.text, 'pos_tag': token.pos_} for token in doc]
        ner = [{'entity': ent.text, 'label': ent.label_} for ent in doc.ents]
        embeddings = [token.vector.tolist() for token in doc]

        return {
        "pos_tags": pos_tags,
        "ner": ner,
        "embeddings": embeddings
        }
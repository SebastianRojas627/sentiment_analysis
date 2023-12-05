from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer

class SentimentAnalyzer:
    def __init__(self):
        model = AutoModelForSequenceClassification.from_pretrained('karina-aquino/spanish-sentiment-model')
        tokenizer = AutoTokenizer.from_pretrained('karina-aquino/spanish-sentiment-model')
        self.sentiment_analysis = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

    def analyse_sentiment(self, text):
        result = self.sentiment_analysis(text)[0]
        label = result['label']
        score = result['score']

        return {"label": label, "score": score}
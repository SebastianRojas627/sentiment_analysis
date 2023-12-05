from fastapi import (
    FastAPI,
    Depends,
    HTTPException
    )
from fastapi.responses import Response
import uvicorn
from pydantic import BaseModel
from config import get_settings
from sentiment_analyzer import SentimentAnalyzer
from text_analizer import TextAnalyzer
from reports import Reports
from starlette.middleware.cors import CORSMiddleware
from datetime import datetime

SETTINGS = get_settings()
sentiment_analysis = SentimentAnalyzer()
text_anaysis = TextAnalyzer()
reports = Reports()

app = FastAPI(
    title=SETTINGS.service_name,
    version=SETTINGS.k_revision
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SentimentAnalysisInput(BaseModel):
    text: str

class TextAnalysisInput(BaseModel):
    text: str

class SentimentAnalysisOutput(BaseModel):
    label: str
    score: float
    processing_time: float

class TextAnalysisOutput(BaseModel):
    sentiment: SentimentAnalysisOutput
    processing_time: float
    pos_tags: list[dict]
    ner: list[dict]
    embeddings: list[list[float]]

def get_sentiment_analysis():
    return sentiment_analysis

def get_text_analysis():
    return text_anaysis

def get_reports():
    return reports

def create_report_entry(time, text, label, score, ex_time):
    entry = {
        "Time and Date of Analysis": time,
        "Text to analyse": text,
        "Label": label,
        "Score": score,
        "Execution Time": ex_time,
        "Sentiment Model": "karina-aquino/spanish-sentiment-model",
        "Text Model": "es_core_news_sm"
    }
    reports.add_prediction(entry)

@app.get("/status")
def status():
    return {
        "status": "Service is running",
        "service": "Phrase sentiment analyser",
        "models": "Spacy's es_core_news_sm for text analysis and nlptown/bert-base-multilingual0uncased-sentiment model for sentiment analysis of phrases in spanish",
        "author": "Sebastian Rojas Osinaga"
    }


"""
    if not data.text.strip():
        raise HTTPException(status_code=400, detail="Text input cannot be empty")
"""
@app.post("/sentiment-analysis")
async def permorm_sentiment_analysis(data: SentimentAnalysisInput, sentiment_analysis: SentimentAnalyzer = Depends(get_sentiment_analysis)):
    if not data.text.strip():
        raise HTTPException(status_code=400, detail="Text input cannot be empty")
    
    start_time = datetime.now()
    text = data.text
    result = sentiment_analysis.analyse_sentiment(text)
    end_time = datetime.now()
    processing_time = (end_time - start_time).total_seconds()
    time = {"processing time": processing_time}
    create_report_entry(start_time, text, result["label"], result["score"], processing_time)

    return result, time

@app.post("/text-analysis")
async def permorm_text_analysis(data: TextAnalysisInput, sentiment_analysis: SentimentAnalyzer = Depends(get_sentiment_analysis), text_analysis: TextAnalyzer = Depends(get_text_analysis)):
    if not data.text.strip():
        raise HTTPException(status_code=400, detail="Text input cannot be empty")
    
    start_time = datetime.now()
    text = data.text
    sentiment = sentiment_analysis.analyse_sentiment(text)
    analysis = text_analysis.analyse_text(text)
    end_time = datetime.now()
    processing_time = (end_time - start_time).total_seconds()
    time = {"processing time": processing_time}
    create_report_entry(start_time, text, sentiment["label"], sentiment["score"], processing_time)

    return sentiment, time, analysis

@app.get("/reports")
def get_reports(reports: Reports = Depends(get_reports)):
    report = reports.generate_report()
    return Response(content=report, media_type="text/csv")    

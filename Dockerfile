FROM python:3.10-slim

ENV PORT 8000

COPY requirements.txt /
RUN pip install -r requirements.txt

RUN python -m spacy download es_core_news_md
RUN python -c "from transformers import AutoModel; AutoModel.from_pretrained('karina-aquino/spanish-sentiment-model')"

COPY ./src/ /src

EXPOSE 8000

CMD ["uvicorn", "sentiment_analysis:app", "--host", "0.0.0.0", "--port", ${PORT}]

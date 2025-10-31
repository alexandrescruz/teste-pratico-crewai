from fastapi import FastAPI, Query
from app.crew_config import run_article_generation
from app.models.article_model import Article

app = FastAPI(title="Multiagent Article Generator - Gemini Edition")

@app.get("/")
def root():
    return {"message": "API de geração de artigos multiagente com Gemini ativa!"}

@app.post("/generate/", response_model=Article)
def generate_article(topic: str = Query(..., description="Tema do artigo")):
    article = run_article_generation(topic)
    return article

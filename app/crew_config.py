import os
from dotenv import load_dotenv
from crewai import Crew
from app.agents.researcher_agent import ResearcherAgent
from app.agents.writer_agent import WriterAgent
from app.models.article_model import Article


def run_article_generation(topic: str):
    # Inicializa os agentes
    researcher = ResearcherAgent()
    writer = WriterAgent()

    # Cria a Crew (sistema multiagente)
    crew = Crew(
        agents=[researcher, writer],
        verbose=True
    )

    # Fluxo da geração
    context = researcher.research_topic(topic)
    content = writer.write_article(topic, context)

    # Retorna um objeto Pydantic formatado
    article = Article(topic=topic, content=context)
    return article

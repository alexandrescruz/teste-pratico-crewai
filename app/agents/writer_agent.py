from crewai import Agent
from dotenv import load_dotenv
import os
load_dotenv()




class WriterAgent(Agent):
    def __init__(self):
        super().__init__(
            name="WriterAgent",
            role="Escritor de Artigos",
            goal="Escrever artigos claros, informativos e bem estruturados com base nas informações fornecidas.",
            backstory="Este agente cria artigos bem estruturados com base em informações confiáveis fornecidas pelo ResearcherAgent.",
            verbose=True,
        )
        

    def write_article(self, topic: str, research: str) -> str:
        result ="""
        Gera um artigo bem estruturado usando a LLM a partir do tópico e do conteúdo pesquisado.
        """
        prompt = f"""
Você é um escritor profissional. Com base nas informações abaixo, escreva um artigo bem estruturado.

Tópico: {topic}
Informações da pesquisa: {research}

O artigo deve ter pelo menos 300 palavras, ser claro, informativo e coeso.
"""
        return result


from crewai import Agent
from app.tools.wikipedia_tool import WikipediaTool

class ResearcherAgent(Agent):
    def __init__(self):
        super().__init__(
            name="ResearcherAgent",
            role="Pesquisador de Conteúdo",
            goal="Pesquisar informações relevantes sobre o tema usando a Wikipedia.",
            backstory="Este agente pesquisa informações precisas e relevantes sobre um determinado tema usando ferramentas de busca confiáveis.",
            tools=[WikipediaTool()],
            verbose=True
        )

    def research_topic(self, topic: str) -> str:
        tool = WikipediaTool()
        return tool._run(topic)

# crewai-desafio

Projeto de demonstração de geração de artigos multiagente usando CrewAI e FastAPI.

Estrutura principal:
- [run.py](run.py) — entrypoint de execução.
- [requirements.txt](requirements.txt) — dependências do projeto.
- [.env](.env) — variáveis de ambiente (API keys).
- [app/main.py](app/main.py) — FastAPI + rotas (`[`app.main.app`](app/main.py)`, [`app.main.generate_article`](app/main.py)`, [`app.main.root`](app/main.py)).
- [app/crew_config.py](app/crew_config.py) — orquestração dos agentes (`[`app.crew_config.run_article_generation`](app/crew_config.py)`).
- [app/models/article_model.py](app/models/article_model.py) — modelo Pydantic (`[`app.models.article_model.Article`](app/models/article_model.py)`).
- [app/agents/researcher_agent.py](app/agents/researcher_agent.py) — agente pesquisador (`[`app.agents.researcher_agent.ResearcherAgent`](app/agents/researcher_agent.py)` / método `research_topic`).
- [app/agents/writer_agent.py](app/agents/writer_agent.py) — agente escritor (`[`app.agents.writer_agent.WriterAgent`](app/agents/writer_agent.py)` / método `write_article`).
- [app/tools/wikipedia_tool.py](app/tools/wikipedia_tool.py) — ferramenta de pesquisa (`[`app.tools.wikipedia_tool.WikipediaTool`](app/tools/wikipedia_tool.py)`).

Visão geral
- A API expõe:
  - GET `/` — saudação (`[`app.main.root`](app/main.py)`).
  - POST `/generate/` — gera artigo a partir de um tópico, retorna o modelo [`app.models.article_model.Article`](app/models/article_model.py) (`[`app.main.generate_article`](app/main.py)`).

Instalação
```bash
pip install -r 
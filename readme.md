# crewai-desafio

Projeto de demonstração de geração de artigos multiagente usando CrewAI e FastAPI.

Resumo rápido
- API REST que expõe endpoints para gerar artigos a partir de um tópico.
- Arquitetura com dois agentes: pesquisador (pesquisa na Wikipedia) e escritor (gera o texto final).

Arquivos principais
- [run.py](run.py) — ponto de entrada (`python run.py`).
- [app/main.py](app/main.py) — FastAPI e rotas (`[`app.main.app`](app/main.py)`, [`app.main.generate_article`](app/main.py)`, [`app.main.root`](app/main.py)).
- [app/crew_config.py](app/crew_config.py) — orquestração dos agentes (`[`app.crew_config.run_article_generation`](app/crew_config.py)`).
- [app/models/article_model.py](app/models/article_model.py) — modelo Pydantic (`[`app.models.article_model.Article`](app/models/article_model.py)`).
- [app/agents/researcher_agent.py](app/agents/researcher_agent.py) — agente pesquisador (`[`app.agents.researcher_agent.ResearcherAgent`](app/agents/researcher_agent.py)` / `research_topic`).
- [app/agents/writer_agent.py](app/agents/writer_agent.py) — agente escritor (`[`app.agents.writer_agent.WriterAgent`](app/agents/writer_agent.py)` / `write_article`).
- [app/tools/wikipedia_tool.py](app/tools/wikipedia_tool.py) — ferramenta de pesquisa (`[`app.tools.wikipedia_tool.WikipediaTool`](app/tools/wikipedia_tool.py)`).

Todos os arquivos no workspace
- [.env](.env)  
- [.gitignore](.gitignore)  
- [readme.md](readme.md)  
- [requirements.txt](requirements.txt)  
- [run.py](run.py)  
- [app/main.py](app/main.py)  
- [app/crew_config.py](app/crew_config.py)  
- [app/models/article_model.py](app/models/article_model.py)  
- [app/agents/researcher_agent.py](app/agents/researcher_agent.py)  
- [app/agents/writer_agent.py](app/agents/writer_agent.py)  
- [app/tools/wikipedia_tool.py](app/tools/wikipedia_tool.py)

Pré-requisitos
- Python 3.10+ (recomendado)
- Instale dependências:
```bash
pip install -r [requirements.txt](http://_vscodecontentref_/0)

Variáveis de ambiente

Configure chaves em .env: GEMINI_API_KEY, MODEL_PROVIDER, MODEL_NAME, OPENAI_API_KEY. Não comitar chaves.
Executando

Iniciar servidor de desenvolvimento:

python [run.py](http://_vscodecontentref_/1)

A API ficará em http://localhost:8000/
Endpoints principais

GET / — saudação ([app.main.root](app/main.py)).
POST /generate/ — gera artigo a partir de um tópico (retorna app.models.article_model.Article). Exemplo:

curl -X POST "http://localhost:8000/generate/?topic=Brasil" -H "Content-Type: application/json"

Fluxo interno (alto nível)

A rota app.main.generate_article chama app.crew_config.run_article_generation.
app.agents.researcher_agent.ResearcherAgent usa app.tools.wikipedia_tool.WikipediaTool para obter contexto.
app.agents.writer_agent.WriterAgent gera o artigo com base no contexto.
Resultado é retornado como app.models.article_model.Article.
Como estender

Adicione novas ferramentas em app/tools/ e registre-as nos agentes.
Implemente chamadas reais à LLM em WriterAgent.write_article para substituir o placeholder atual.
Adicione testes e validações no modelo Pydantic (app/models/article_model.py).

Observações

A implementação do Writer ainda retorna um placeholder; integrar a LLM (via CrewAI/SDK) é o próximo passo.
A Wikipedia requer header User-Agent (já presente em app.tools.wikipedia_tool.WikipediaTool).
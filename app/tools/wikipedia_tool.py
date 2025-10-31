import requests
from crewai_tools import RagTool


class WikipediaTool(RagTool):
    name: str = "Wikipedia Search Tool"
    description: str = "Consulta a API da Wikipedia e retorna texto limpo sobre um tópico"

    def _run(self, topic: str) -> str:
        try:
            url = "https://pt.wikipedia.org/w/api.php"
            params = {
                "action": "query",
                "prop": "extracts",
                "exlimit": 1,
                "explaintext": 1,
                "titles": topic,
                "format": "json",
                "utf8": 1,
                "redirects": 1
            }

            # 🔥 CABEÇALHO OBRIGATÓRIO PARA WIKIPEDIA
            headers = {
                "User-Agent": "CrewAI-Bot/1.0 (https://github.com/seu-projeto; contato@seudominio.com)"
            }

            response = requests.get(url, params=params, headers=headers, timeout=10)
            response.raise_for_status()

            data = response.json()
            pages = data.get("query", {}).get("pages", {})

            for page in pages.values():
                extract = page.get("extract")
                if extract:
                    return extract

            return "Nenhuma informação encontrada."

        except requests.exceptions.RequestException as e:
            return f"Erro ao consultar Wikipedia: {e}"




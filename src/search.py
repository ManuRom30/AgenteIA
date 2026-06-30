import os
from tavily import TavilyClient


def web_search(query: str, max_results: int = 3) -> str:
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        return ""

    client = TavilyClient(api_key=api_key)
    try:
        response = client.search(
            query=query,
            search_depth="basic",
            max_results=max_results,
            include_answer=True,
        )
        results = []
        if response.get("answer"):
            results.append(f"Resumen: {response['answer']}")
        for r in response.get("results", []):
            results.append(f"- {r['title']}: {r['content'][:200]}")
        return "\n".join(results)
    except Exception:
        return ""


def needs_web_search(query: str) -> bool:
    keywords = [
        "arancel", "aranceles", "tratado", "tlc", "regulacion",
        "normativa", "restriccion", "pais", "acuerdo comercial",
        "partida arancelaria", "subpartida", "impuesto importacion",
        "requisitos para exportar a", "regulacion en",
    ]
    query_lower = query.lower()
    return any(kw in query_lower for kw in keywords)

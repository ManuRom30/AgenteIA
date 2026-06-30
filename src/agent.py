from langchain_openai import ChatOpenAI

from src.vectorstore import get_vectorstore
from src.prompts import SYSTEM_PROMPT
from src.search import web_search, needs_web_search


def get_response(query: str, chat_history: list, retriever, llm) -> str:
    docs = retriever.invoke(query)
    context = "\n\n---\n\n".join([doc.page_content for doc in docs])

    web_context = ""
    if needs_web_search(query):
        web_result = web_search(f"exportacion textil Colombia {query}")
        if web_result:
            web_context = f"\n\n## Informacion actualizada de internet:\n{web_result}"

    full_context = context + web_context

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT.format(context=full_context)},
    ]

    for msg in chat_history:
        messages.append({"role": msg["role"], "content": msg["content"]})

    messages.append({"role": "user", "content": query})

    response = llm.invoke(messages)
    return response.content

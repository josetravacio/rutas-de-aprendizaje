# Contenido COMPLETO para agentes/concise_search.py

from duckduckgo_search import DDGS

def concise_search(query: str, max_num_results: int = 1):
  """
  Realiza una búsqueda web real usando DuckDuckGo y devuelve el resultado
  más relevante en un formato estructurado (título, enlace y resumen).
  """
  print(f"🔎 Herramienta concise_search: Buscando en la web '{query}'...")

  try:
    results = DDGS().text(
        query,
        region='wt-wt',
        safe_search='off',
        max_results=max_num_results
    )

    if not results:
      return "No se encontraron resultados en la web para la búsqueda."

    formatted_output = ""
    for result in results:
        formatted_output += f"Título: {result['title']}\n"
        formatted_output += f"Enlace: {result['href']}\n"
        formatted_output += f"Resumen: {result['body']}\n\n"

    return formatted_output.strip()

  except Exception as e:
    print(f"❌ ERROR en concise_search: {e}")
    return "Error: No se pudo completar la búsqueda en la web."
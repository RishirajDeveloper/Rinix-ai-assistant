import requests
from bs4 import BeautifulSoup
from googlesearch import search

def RealtimeSearchEngine(query):
    """
    Performs real-time web search and returns summarized results.
    """
    try:
        # Use Google search to get relevant URLs
        search_results = list(search(query, num_results=3))

        if not search_results:
            return "No search results found."

        # Get content from the first result
        response = requests.get(search_results[0], timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract title and first few paragraphs
        title = soup.title.string if soup.title else "No title found"
        paragraphs = soup.find_all('p')[:3]  # Get first 3 paragraphs
        content = ' '.join([p.get_text() for p in paragraphs])

        # Summarize the content
        summary = f"Title: {title}\n\nSummary: {content[:500]}..." if len(content) > 500 else f"Title: {title}\n\nSummary: {content}"

        return summary

    except Exception as e:
        return f"Error performing search: {str(e)}"

import feedparser
import urllib.parse

ARXIV_API = "http://export.arxiv.org/api/query"

def _build_url(query: str, sort_by: str, max_results: int) -> str:
    params = {
        "search_query": f"all:{query}",
        "start": 0,
        "max_results": max_results,
        "sortBy": sort_by,
        "sortOrder": "descending",
    }
    return f"{ARXIV_API}?{urllib.parse.urlencode(params)}"


def fetch_papers(query: str, arxiv_config: dict):
    recent_count = arxiv_config.get("recent", 10)
    relevant_count = arxiv_config.get("relevant", 10)

    urls = [
        _build_url(query, "submittedDate", recent_count),
        _build_url(query, "relevance", relevant_count),
    ]

    papers = {}
    for url in urls:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            arxiv_id = entry.id.split("/abs/")[-1]
            papers[arxiv_id] = entry

    return list(papers.values())
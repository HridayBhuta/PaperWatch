def filter_papers(papers, keywords):
    filtered = []

    for paper in papers:
        text = (paper["title"] + paper["summary"]).lower()

        if any(k.lower() in text for k in keywords):
            if "survey" not in paper["title"].lower():
                filtered.append(paper)

    return filtered
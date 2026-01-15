import os
import requests
import logging

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def paper_exists(paper_id, download_dir):
    filename = f"{paper_id}.pdf"
    return os.path.exists(os.path.join(download_dir, filename))

def get_pdf_url(paper):
    """Extract PDF URL from arxiv feed entry links."""
    for link in paper.get("links", []):
        if link.get("type") == "application/pdf":
            return link.get("href")

    arxiv_id = paper["id"].split("/abs/")[-1]
    return f"https://arxiv.org/pdf/{arxiv_id}.pdf"

def download_paper(paper, download_dir):
    ensure_dir(download_dir)

    arxiv_id = paper["id"].split("/abs/")[-1]
    filename = f"{arxiv_id.replace('/', '_')}.pdf"
    filepath = os.path.join(download_dir, filename)

    if os.path.exists(filepath):
        logging.info(f"Skipping already downloaded paper: {arxiv_id}")
        return False

    logging.info(f"Downloading paper: {paper['title']}")
    pdf_url = get_pdf_url(paper)
    response = requests.get(pdf_url, timeout=30)

    if response.status_code == 200:
        with open(filepath, "wb") as f:
            f.write(response.content)
        return True
    else:
        logging.warning(f"Failed to download {arxiv_id}")
        return False
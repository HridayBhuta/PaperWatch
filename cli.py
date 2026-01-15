import argparse
import logging
from config import load_config
from utils import setup_logging
from fetchers.arxiv import fetch_papers
from filters import filter_papers
from storage import download_paper

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", required=False, help="Topic to search for. If not provided, searches all keywords from config.")
    args = parser.parse_args()

    config = load_config()
    setup_logging(config["logging"]["file"])

    topics = [args.topic] if args.topic else config["keywords"]

    all_papers = []
    for topic in topics:
        logging.info(f"Starting PaperWatch for topic: {topic}")
        papers = fetch_papers(topic, config["arxiv"])
        all_papers.extend(papers)

    unique_papers = {paper["id"]: paper for paper in all_papers}
    filtered = filter_papers(list(unique_papers.values()), config["keywords"])

    for paper in filtered:
        download_paper(
            paper,
            config["storage"]["download_path"]
        )

    logging.info("PaperWatch run completed")

if __name__ == "__main__":
    main()
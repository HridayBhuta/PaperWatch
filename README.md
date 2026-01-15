# PaperWatch

An automated research paper tracker that fetches, filters, and downloads papers from arXiv based on your interests.

## Features

- **Automated Paper Discovery**: Fetches papers from arXiv sorted by both recency and relevance
- **Keyword Filtering**: Filters papers based on configurable keywords of interest
- **Automatic Downloads**: Downloads matching papers as PDFs to your specified directory
- **Deduplication**: Automatically removes duplicate papers across multiple searches
- **Survey Filter**: Excludes survey papers to focus on original research
- **Cron Support**: Easily schedule automated runs with included cron scripts
<!-- - **Email Notifications**: Built-in email notification support (optional) -->

## Installation

### Prerequisites

- Python 3.12+
- Poetry (recommended) or pip

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/HridayBhuta/PaperWatch.git
   cd PaperWatch
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

   Or using pip:
   ```bash
   pip install feedparser pyyaml tenacity requests
   ```

3. Create your configuration file:
   ```bash
   cp config/config.yaml.example config/config.yaml
   ```

4. Edit `config/config.yaml` with your preferences (see [Configuration](#configuration))

## Usage

### Basic Usage

Search for a specific topic:
```bash
poetry run python cli.py --topic "machine learning"
```

Search for all keywords defined in your config:
```bash
poetry run python cli.py
```

### Configuration

Edit `config/config.yaml` to customize PaperWatch:

```yaml
keywords:
  - artificial intelligence
  - machine learning   # Can choose how many ever keywords

arxiv:
  recent: 10      # Number of recent papers to fetch
  relevance: 10   # Number of relevant papers to fetch

storage:
  download_path: downloads/papers

logging:
  file: logs/paperwatch.log
```

### Automated Runs with Cron

1. Create your run script from the example:
   ```bash
   cp cron/run.sh.example cron/run.sh
   ```

2. Edit `cron/run.sh` to set your paths and keywords:
   ```bash
   PROJECT_ROOT="full/path/to/repo"
   PYTHON="full/path/to/python"
   KEYWORDS=("machine learning" "deep learning" "transformers")
   ```

3. Make it executable:
   ```bash
   chmod +x cron/run.sh
   ```

4. Add a cron job:
   ```bash
   # Runs daily at 9 AM
   0 9 * * * /path/to/paperwatch/cron/run.sh
   ```

## Project Structure

```
paperwatch/
├── cli.py
├── config.py
├── filters.py
├── storage.py
├── utils.py
├── fetchers/
│   └── arxiv.py
├── config/
│   └── config.yaml.example
├── cron/
│   ├── run.sh.example
│   └── paperwatch.cron
├── downloads/
└── logs/
```

## How It Works

1. **Fetch**: Queries arXiv API for papers matching your topics, sorted by submission date and relevance
2. **Deduplicate**: Removes duplicate papers that appear in multiple searches
3. **Filter**: Keeps only papers containing your keywords in title/abstract, excludes surveys
4. **Download**: Saves matching papers as PDFs to your download directory

## License

MIT License - see [LICENSE](LICENSE) for details.
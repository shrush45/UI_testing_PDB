# UI Testing — RCSB Protein Data Bank (PDB)

Automated UI tests for the [RCSB PDB website](https://www.rcsb.org/) using Selenium WebDriver and Python.

## Tech Stack

- Python
- Selenium
- WebDriver Manager

## Setup

```bash
git clone https://github.com/shrush45/UI_testing_PDB.git
cd UI_testing_PDB
pip install -r requirements.txt
```

## Running Tests

```bash
python -m pytest tests/
```

## Project Structure

```
UI_testing_PDB/
├── tests/          # Test scripts
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.x
- Google Chrome (WebDriver Manager handles the ChromeDriver automatically)
# Nova Financial Solutions Analysis
This repository contains data analysis projects focusing on financial news and stock price datasets. The repository includes notebooks for exploratory data analysis (nova_eda), stock price analysis, datasets, unit tests, and configuration files for continuous integration.

## Repository Structure
```
.
├── notebook
│   ├── __init__.py
│   └── nova_eda.ipynb
│   └── stock_price_fetch.ipynb
│   └── README.md
├── data
│   ├── raw_analyst_ratings.csv
├── tests
│   ├── __init__.py
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── descriptive_statistics.py
│   ├── publisher_analysis.py
│   ├── text_analysis.py
│   ├── time_series_analysis.py
├── requirements.txt
└── .github
    └── workflows
        └── unittests.yml
```

## Files Overview
* notebook/nova_eda.ipynb: Jupyter Notebook containing exploratory data analysis, Quantitative analysis and Correlation between news and stock movement for the raw_analyst_rating dataset.
* src/main.py: python file containing exploratory data analysis for the raw_analyst_rating dataset.
* data/:
    + raw_analyst_ratings.csv
* tests: 
* requirements.txt: List of required Python packages for running the project.
* .github/workflows/unittests.yml: GitHub Actions workflow file for running unit tests on push events.
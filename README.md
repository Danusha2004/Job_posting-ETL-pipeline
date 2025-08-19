# JOB POSTING ETL PIPELINE
A production-ready, end-to-end pipeline that extracts job postings, cleans & normalizes fields (title, company, location, salary, skills), and loads the curated data into MySQL for analytics. A Power BI report connects to MySQL to visualize role demand, top hiring companies, salary trends, and more.

## Features

API-based extraction: Uses Adzuna Job Search API (free/public source) to fetch live job postings.

ETL: Extract → Save intermediate as CSV → Transform (cleaning, standardization) → Load into MySQL

Schema: Relational model for jobs, companies, description, and locations

Analytics: Power BI dashboards (Job Count by Role, Top Hiring Companies)

Reproducible: requirements.txt, .env config, and scripts for one-command runs

Quality: Data-quality checks (nulls, ranges, duplicates)

Generic-ready: Can be extended to any job posting API, CSV dataset, or streaming job feed.

## 🧱 Architecture
``` bash
[Adzuna API]
     │  Extract (Python)
     ▼
   jobs_raw.csv (intermediate)
     │  Transform (clean, parse, standardize, enrich)
     ▼
   /etl/transform.py → Clean Zone (/data/clean)
     │  Load
     ▼
   MySQL (analytics schema)
     │
     ▼
   Power BI (Direct / Import Mode) → Dashboards & DAX
```
   
## 🧰 Tech Stack
``` bash

Python 3.9+

Requests, Pandas, SQLAlchemy, python-dotenv

MySQL 8+

Power BI Desktop (for visualization)
```
Optional (for future upgrades): Airflow/Prefect for orchestration, Docker for reproducibility, Tableau as alternative BI.

📁 Project Structure

```bash
job-posting-etl/
├─ etl/
│  └─ extract_api.py        # fetch from Adzuna API
├─ sql/
│  └─ job_postings.sql
├─ data/
│  ├─ raw/                  # API extracts (CSV)
│  └─ clean/                # cleaned outputs (intermediate)
├─ powerbi/
│  └─ JobPostingReport.pbix # Power BI file
├─ .env.example
├─ requirements.txt
└─ README.md
```
🔗 Data Source: Adzuna API

## Why Adzuna? Unlike Naukri/LinkedIn (protected with anti-scraping, CAPTCHA, and dynamic content), Adzuna offers a developer-friendly REST API to fetch job listings.

Endpoint Example:
https://api.adzuna.com/v1/api/jobs/in/search/1?app_id=YOUR_APP_ID&app_key=YOUR_APP_KEY&results_per_page=50&what=Data%20Analyst&where=India

Parameters allow filtering by keywords, location, salary range, etc.
Extracted data is stored in CSV (jobs_raw.csv) for reproducibility.

## What Makes This Project Stand Out

Real-world challenge addressed: Job boards block scraping → API-based solution ensures compliance.

Lightweight pipeline: Only one script (extract.py) and CSV-based staging.

Analytics-ready: MySQL + Power BI for insights.

Extensible: Can add transforms, orchestration, or more APIs later.

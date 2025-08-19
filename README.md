A production-ready, end-to-end pipeline that extracts job postings, cleans & normalizes fields (title, company, location, salary, skills), and loads the curated data into MySQL for analytics. A Power BI report connects to MySQL to visualize role demand, top hiring companies, salary trends, and more.

✨ Features

ETL: Extract from CSV/JSON/API → Transform (cleaning, standardization) → Load into MySQL

Schema: Opinionated relational model for jobs, companies, skills, and locations

Analytics: Power BI dashboards (Job Count by Role, Top Hiring Companies, Salary vs Experience)

Reproducible: requirements.txt, .env config, and scripts for one-command runs

Quality: Basic data-quality checks (nulls, ranges, duplicates)

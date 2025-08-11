import requests
import pandas as pd
import time

APP_ID = "26eaa9751"  # Replace with your Application ID
APP_KEY = "b5b7b9fb9za26b9b0121078d9f8c764799"  # Replace with your Application Key


COUNTRY = "in"  # 'in' for India, 'gb' for UK, etc.
SEARCH_TERMS = ["developer", "data analyst", "cybersecurity", "manager"]
RESULTS_PER_PAGE = 20  # Max is 50
MAX_PAGES = 5  # Limit pages per role (to avoid hitting free tier limit)

all_jobs = []

for term in SEARCH_TERMS:
    print(f"Scraping jobs for: {term}")
    for page in range(1, MAX_PAGES + 1):
        url = f"https://api.adzuna.com/v1/api/jobs/{COUNTRY}/search/{page}"
        params = {
            "app_id": APP_ID,
            "app_key": APP_KEY,
            "results_per_page": RESULTS_PER_PAGE,
            "what": term,
            "content-type": "application/json"
        }
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print(f"Error fetching page {page} for {term}: {response.status_code}")
            break

        data = response.json()
        jobs = data.get("results", [])
        if not jobs:
            break

        for job in jobs:
            all_jobs.append({
                "title": job.get("title"),
                "company": job.get("company", {}).get("display_name"),
                "location": job.get("location", {}).get("display_name"),
                "Salary": job.get("Salary",{}).get("display_name"),
                "created": job.get("created"),
                "description": job.get("description"),
                "redirect_url": job.get("redirect_url")
            })

        # Small delay to avoid hitting rate limits
        time.sleep(0.5)

df = pd.DataFrame(all_jobs)
print(f"\nTotal Jobs Collected: {len(df)}")
df.to_csv("adzuna_jobs.csv", index=False, encoding="utf-8")
print("Saved to adzuna_jobs.csv")

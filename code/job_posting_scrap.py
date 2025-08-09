import requests
import pandas as pd
import time

API_KEY = "a681c95436msha21de5c822b24ddp1c6689jsn816fcb8b7f60"  # Replace with your JSearch API key
BASE_URL = "https://jsearch.p.rapidapi.com/search"

headers = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": "jsearch.p.rapidapi.com"
}

roles = ["Python Developer", "Software Developer", "Cybersecurity", "Data Analyst"]
locations = ["Bangalore", "Chennai", "Mumbai", "Delhi", "Hyderabad", "Pune", "Kolkata", "India"]

all_jobs = []

for role in roles:
    for location in locations:
        for page in range(1, 4):  # Increase pages to get more results
            params = {
                "query": f"{role} in {location}",
                "page": page,
                "num_pages": 1
            }
            
            response = requests.get(BASE_URL, headers=headers, params=params)
            if response.status_code == 200:
                data = response.json()
                jobs = data.get("data", [])
                
                for job in jobs:
                    all_jobs.append({
                        "search_role": role,
                        "search_location": location,
                        "title": job.get("job_title"),
                        "company": job.get("employer_name"),
                        "location": job.get("job_city"),
                        "via": job.get("job_publisher"),
                        "job_type": job.get("job_employment_type"),
                        "salary": job.get("job_salary"),
                        "description": job.get("job_description"),
                        "posted_at": job.get("job_posted_at_datetime_utc"),
                        "apply_link": job.get("job_apply_link")
                    })
            
            time.sleep(1)  # Avoid rate limiting

df = pd.DataFrame(all_jobs)
df.to_csv("jobs_india.csv", index=False)
print(f"Saved {len(df)} jobs to jobs_india.csv")

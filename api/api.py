import requests

API_KEY = '91e7bcca5f07d95dbf540d18d41e1033	'
API_ID = '501f4066'
url = f"https://api.adzuna.com/v1/api/jobs/us/search/1?app_id={API_ID}&app_key={API_KEY}"

response =  requests.get(url)
data = response.json()

for job in data['results']:
    title = job['title']
    description = job['description']
    requirements = job.get('requirements')

    print(f"Title: {title}")
    print(f"Description: {description}")
    print(f"Requirements: {requirements}")
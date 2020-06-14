import glassdoor_scraper as gs
import pandas as pd

path = "/home/vishnub/chromedriver"

df = gs.get_jobs('Data Scientist', 1000, False, path, 15)

df.head()
df.to_csv('glassdoor_jobs.csv', index=False)

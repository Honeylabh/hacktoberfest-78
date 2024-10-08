 Import necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

 Step 1: Make a request to the website
url = "https://example.com"  # Replace with the website you want to scrape
response = requests.get(url)

Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

Step 3: Extract specific data (in this case, all titles from <h2> tags)
titles = soup.find_all("h2")

Step 4: Store the extracted titles in a list
titles_list = [title.text.strip() for title in titles]

Step 5: Optionally, save the data to a CSV using pandas
df = pd.DataFrame(titles_list, columns=["Title"])
df.to_csv("scraped_titles.csv", index=False)

print("Scraped titles saved to 'scraped_titles.csv'")

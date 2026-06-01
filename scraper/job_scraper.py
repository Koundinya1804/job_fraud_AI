import requests
from bs4 import BeautifulSoup


def scrape_job_description(url):

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = soup.find_all("p")

        job_text = " ".join([p.get_text() for p in paragraphs])

        return job_text

    except:
        return ""
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_and_download_pdfs(base_url, download_dir="pdf_downloads"):
    """Harvest PDF links from a webpage and download them locally."""

    # Create a local landing zone
    os.makedirs(download_dir, exist_ok=True)

    # Retrieve source HTML
    response = requests.get(base_url, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    pdf_links = set()

    # Capture all PDF endpoints
    for link in soup.find_all("a", href=True):
        href = link["href"]
        if href.lower().endswith(".pdf"):
            pdf_links.add(urljoin(base_url, href))

    # Execute asset pull-down
    for pdf_url in pdf_links:
        filename = pdf_url.split("/")[-1]
        local_path = os.path.join(download_dir, filename)

        try:
            pdf_data = requests.get(pdf_url, timeout=15)
            pdf_data.raise_for_status()

            with open(local_path, "wb") as f:
                f.write(pdf_data.content)

            print(f"Downloaded: {filename}")

        except Exception as e:
            print(f"Failed: {pdf_url} — {e}")

    return pdf_links


# Example execution:
if __name__ == "__main__":
    url = "https://www.udemy.com/course/ccna-complete/learn"
    scrape_and_download_pdfs(url)

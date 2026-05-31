from curl_cffi import requests
from bs4 import BeautifulSoup
from curl_cffi.curl import CurlOpt

def scraper():
    print("==========================================")
    urlnk = input("\nEnter a url you would like to scrape: ").strip()
    while not urlnk.startswith("http"):
        urlnk = input("\nPlease enter a valid url (starting with http/https): ").strip()


    print(f"Fetching data from ", urlnk, "...")    
   
    try:
        session =requests.Session(curl_options={CurlOpt.IPRESOLVE:1})
        response = session.get(urlnk, impersonate="chrome", timeout=15)
    except Exception as e:
        print("Connection Error: ", e)
        return None


    if response.status_code != 200:
        print("Error! Failed to retrieve page. Status code:", response.status_code)
        return None


    soup = BeautifulSoup(response.text, "html.parser")
    article = soup.find("article") or soup.find("body")


    if not article:
        print("Could not find the content of this page, sorry.")
        return None


    h1_tag = article.find('h1')
    page_title = h1_tag.text.strip() if h1_tag else "No Title"
    print(f"\n==================== Title: ", page_title, " ====================\n")


    for tag in article.find_all(['h2', 'h3', 'h4','h5','h6', 'p', 'code', 'a', 'blockquote', 'ul', 'ol', 'li','link']):
        text = tag.text.strip()
        if not text:
            continue
            
        if tag.name in ['h2', 'h3']:
            print(f"\n--- {text} ---")
        elif tag.name == 'code':
            print("\n")
            print(f"  [Code Block]: {text}")
            print("\n")
        elif tag.name == "ul":
            print("\n")
            print(f"  [Unordered List]: {text}")
            print("\n")
        elif tag.name == "ol":
            print("\n")
            print(f"  [Ordered List]: {text}")
            print("\n")
        else:
            print("\n")
            print(text)
            print("\n")


if __name__ == "__main__":
    scraper()

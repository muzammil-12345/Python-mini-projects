'''
  Day 21: Wikipedia Article Scrapper Using Web Scrapping
  Topics Covered:
  1. What is Web scraping?
  2. Understanding HTML Structure
  3. Using Requests to fetch web pages
 4. Using beautifulSoup for parsing
  5. Mini-project: wikipedia Article Scrapper
  '''

# What is web scraping?
'''Web scraping is the process of extracting information 
from websites. Its commonly used for Data collection,
market research, content Agregation, Automation tasks.
'''

#Understanding HTML structure

''' 
<html>
    <head><title> Sample page </title></head>
    <body>
       <div>
          <h1> Main Title </h1>
          <p> This is a paragraph </p>
          <a> href="https://example.com">Click here</a>
       </div>
    </body>
</html>
'''

# #Using Requests to fetch Web pages
# #Sample website: https://en.wikipedia.org/wiki/Python_(programming language)

# Import requests
# from bs4 import BeautifulSoup


# url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
# headers ("User-Agent": "Mozilla/5.0")
# response = requests.get(url, headers=headers)

# if response.status_code 200:
#   print(response.text[:500])
# else:
#      print(f"Failed to retrive data. Status code: (response.status_code)") 


# # Using BeautifulSoup for parsing (parsing means going through the text one at a time)
# from bs4 import BeautifulSoup

# html_content = <h1> Main Title </h1><p> This is a paragraph </p><a> href="https://example.com'>Click here</a>
# soup BeautifulSoup(html_content, "html.parser")
# print(soup.hl.text)
# print(soup.p.text)


# --- Mini-project: Wikipedia Article Scrapper ---
'''How it woks: Fetches, Read wikipedia article based on user provided
topic. It extracts the title, heading and summary and then finally
displays links to the related topics
'''
import requests
from bs4 import BeautifulSoup

# Step 1: Get wikipedia Article URL
def get_wikipedia_page(topic):
    url = f"https://en.wikipedia.org/wiki/{topic.replace(' ','_')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrive data. Status code: {response.status_code}. Check the topic and try again.")
        return None
    
# Step 2: Extract Article Title    

def get_article_title(soup):
    return soup.find("h1").text

# Step 3: Extract Article Summary
def get_artice_summary(soup):
    paragraphs = soup.find_all('p')
    for para in paragraphs:
        if para.text.strip():
            return para.text.strip()
    return "No summary found" 

# Step 4: Extract Headings
def get_headings(soup):
    headings = [heading.text.strip() for heading in soup.find_all(['h2','h3','h4'])]
    return headings


# Step 5: Extract related links

def get_related_links(soup):
    links = []
    for a_tag in soup.find_all('a',href= True):
        href = a_tag['href']
        if href.startswith('/wiki/') and ':' not in href:
            links.append(f"https://en.wikipedia.org{href}")
    return list(set(links))[:5]

# Step 6: Main program
def main():
    topic = input("Enter a topic to search in wikipedia: ").strip()
    page_content = get_wikipedia_page(topic)

    if page_content:
        soup = BeautifulSoup(page_content,"html.parser")
        title = get_article_title(soup)
        summary = get_artice_summary(soup)
        headings = get_headings(soup)
        related_links = get_related_links(soup)

        print("\n--- Wikipedia Article Detais ---")
        print(f"\nTitle: {title}")
        print(f"\nSummary: {summary}")
        print("\nHeadings:")
        for heading in headings[:5]:
            print(f" - {heading}")

        print("\nRelated Links:")
        for link in related_links:
            print(f"- {link}")

# Run the program
if __name__ =="__main__":
    main()
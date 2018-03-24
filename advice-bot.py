# import libraries
import urllib2
import requests
import feedparser
from bs4 import BeautifulSoup

# specify the url [LPT]
quote_page = feedparser.parse('https://www.reddit.com/r/LifeProTips/.rss')

for x in range(0, 8):
    soup = BeautifulSoup(quote_page['entries'][x]['title'], 'html.parser')
    if soup.get_text()[:4] == 'LPT:':
        print(soup.get_text()[4:].partition(".")[0] + ".\n")

'''
path = quote_page
headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"}
with requests.Session() as s:
    r = s.get(path, headers = headers)
    soup = BeautifulSoup(r.content, "lxml")
    threads = soup.select('a.title.may-blank')
    print(threads)
    
    for a in threads:
        print(a)
       
'''




#python advice-bot.py
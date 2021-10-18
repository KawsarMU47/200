#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# GEtting news from Times of India

toi_r = requests.get("https://www.prothomalo.com/collection/latest")
toi_soup = BeautifulSoup(toi_r.content, 'html5lib')

toi_headings = toi_soup.find_all('h2')

toi_headings #= toi_headings[0:-13] # removing footers

toi_news = []

for th in toi_headings:
    toi_news.append(th.text)



# GEtting news from Times of bangla

tob_r = requests.get("https://bangla.hindustantimes.com/sports/football/saff-championship-2021-when-and-where-to-watch-india-vs-nepal-final-match-on-discovery-plus-31634382507274.html")
tob_soup = BeautifulSoup(tob_r.content, 'html5lib')

tob_headings = tob_soup.find_all('h2')

tob_headings #= toi_headings[0:-13] # removing footers

tob_news = []

for bn in tob_headings:
    tob_news.append(bn.text)


#Getting news from Hindustan times

ht_r = requests.get("https://www.sylhetview24.news/news/312388")
ht_soup = BeautifulSoup(ht_r.content, 'html5lib')
ht_headings = ht_soup.findAll ('h2')#("div", {"class": "headingfour"})
ht_headings = ht_headings[2:]
ht_news = []

for hth in ht_headings:
    ht_news.append(hth.text)



"""
ht_r = requests.get("https://www.banglanews24.com/category/%E0%A6%9C%E0%A6%BE%E0%A6%A4%E0%A7%80%E0%A7%9F/1")
ht_soup = BeautifulSoup(toi_r.content, 'html5lib')

ht_headings = toi_soup.find_all('h2')

ht_headings #= toi_headings[0:-13] # removing footers

ht_news = []

for th in ht_headings:
    ht_news.append(th.text)
"""

def index(req):
    return render(req, 'news/index.html', {'toi_news':toi_news, 'tob_news':tob_news,'ht_news': ht_news})
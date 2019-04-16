from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import requests
import os
import pandas as pd 
import pprint
import pymongo

conn = 'mongodb://localhost:27017'

client = pymongo.MongoClient(conn)
db = client.top10_db

def scrape():

    url = 'https://www.nps.gov/aboutus/visitation-numbers.htm'
    browser = Browser('chrome')
    browser.visit(url)
    html = browser.html

    tables = pd.read_html(html)
    top10list = tables[1]
    top10list  

    db.top10list.insert(top10list.to_dict(orient = "records"))
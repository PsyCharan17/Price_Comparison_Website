

# In[8]:


from bs4 import BeautifulSoup as soup
import requests
from urllib.request import urlopen


# In[9]:


import pandas as pd
import numpy as np


# In[10]:


import csv
from selenium import webdriver


# In[11]:


#keyword=input("Enter product to search: ")


# In[12]:


# url="https://www.flipkart.com/search?q="+keyword
# urlA="https://www.amazon.in/s?k="+keyword


# ## Amazon

# In[14]:


def scrape(urlM):
    if urlM == urlA:
        driver = webdriver.Chrome(
            executable_path="D:\webdrivers\chromedriver.exe")
        driver.get(urlA)
        page_soupA = soup(driver.page_source, "html.parser")
        # print(page_soupA)
        containerA = page_soupA.find_all(
            'div', {'data-component-type': "s-search-result"})
        conA = containerA[0]
        soup.prettify(conA)
        print("-------------------------------------------------")

        for co in containerA:
            atag = co.h2.a
            print(atag.text)
        print("-------------------------------------------------")

        for pr in containerA:
            prA = pr.find('span', 'a-price')

            try:
                priceA = prA('span', 'a-offscreen')
                print(priceA[0].text)

            except(TypeError):
                print()
        print("-------------------------------------------------")

        for rat in containerA:
            try:
                rating = rat.i.text
                print(rating)
            except(AttributeError):
                print()

        print("-------------------------------------------------")
        for rew in containerA:
            try:
                rewC = rew.find(
                    'span', {'class': "a-size-base s-underline-text"})
                print(rewC.text)
            except(AttributeError):
                print()
    elif urlM == url:
        uClient = urlopen(url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        container = page_soup.find_all("div", {"class": "_2kHMtA"})
        con = container[0]
        soup.prettify(con)
        print("-------------------------------------------------")

        for co in container:
            product_name = co.findAll("div", {"class": "_4rR01T"})
            print(product_name[0].text)
        print("-------------------------------------------------")

        for co in container:
            s_price = co.findAll("div", {"class": "_30jeq3 _1_WHN1"})
            print(s_price[0].text)
        print("-------------------------------------------------")

        for co in container:
            rating = co.findAll("span", {"class": "_2_R_DZ"})
            try:
                print(rating[0].text)
            except(IndexError):
                print()
        print("-------------------------------------------------")

        for co in container:
            star = co.findAll("div", {"class": "_3LWZlK"})
            try:
                print(star[0].text)
            except(IndexError):
                print()


keyword = input("Enter product to search: ")
keyword = keyword.replace(" ", "+")

urlA = "https://www.amazon.in/s?k="+keyword
url = "https://www.flipkart.com/search?q="+keyword


print("Connecting to Amazon")
scrape(urlA)
print("Connecting to Flipkart")
scrape(url)

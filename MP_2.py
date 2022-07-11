

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


# keyword=input("Enter product to search: ")


# In[12]:


# url="https://www.flipkart.com/search?q="+keyword
# urlA="https://www.amazon.in/s?k="+keyword


# ## Amazon

# In[14]:


def scrape(urlM, product_info, product_nameList, product_priceList, product_ratingList):

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

        # keysList = ["product_name", "product_info",
        # "product_price", "product_rating"]

        # valuesList = [product_nameList,product_infoList,product_priceList, product_ratingList ]

        #  "product_img": [], "product_name": [], "product_info": [], "product_price": [], "product_rating": []}

        print("-------------------------------------------------")

        for co in containerA[0:5]:
            atag = co.h2.a
            print(atag.text)

            # Adding name of product from Amazon into the list
            title = atag.text
            x = title.find("(")
            res = title[0:x]
            product_nameList.append(res)

        print("-------------------------------------------------")

        for pr in containerA[0:5]:
            prA = pr.find('span', 'a-price')

            try:
                priceA = prA('span', 'a-offscreen')
                print(priceA[0].text)

                # Adding price of product from Amazon into the list

                product_priceList.append(str(priceA[0].text))
            except(TypeError):
                print()
        print("-------------------------------------------------")

        for rat in containerA[0:5]:
            try:
                rating = rat.i.text
                print(rating)
                # Adding ratings of product from Amazon into the list

                if(rating):
                    product_ratingList.append(rating[0:3])
                else:
                    product_ratingList.append("")

            except(AttributeError):
                print()

        print("-------------------------------------------------")
        for rew in containerA[0:5]:
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

        for co in container[0:5]:
            product_name = co.findAll("div", {"class": "_4rR01T"})
            print(product_name[0].text)

            # Adding name of product from Flipkart in the file

            title = product_name[0].text
            x = title.find("(")
            res = title[0:x]
            product_nameList.append(product_name[0].text)

        print("-------------------------------------------------")

        for co in container[0:5]:
            s_price = co.findAll("div", {"class": "_30jeq3 _1_WHN1"})
            print(s_price[0].text)

            # Adding price of product from Flipkart in the file

            product_priceList.append(str(s_price[0].text))
        print("-------------------------------------------------")

        for co in container[0:5]:
            rating = co.findAll("span", {"class": "_2_R_DZ"})
            try:
                print(rating[0].text)

            except(IndexError):
                print()
        print("-------------------------------------------------")

        for co in container[0:5]:
            star = co.findAll("div", {"class": "_3LWZlK"})
            try:
                print(star[0].text)
                stars = str(star[0].text)
                # Adding product rating from Flipkart in the file
                if(stars):
                    product_ratingList.append(stars[0:3])
                else:
                    product_ratingList.append(" ")
            except(IndexError):
                print()

    product_info = {"product_name": product_nameList,
                    "product_price": product_priceList, "product_rating": product_ratingList}
    return product_info


keyword = input("Enter product to search: ")
keyword = keyword.replace(" ", "+")

urlA = "https://www.amazon.in/s?k="+keyword
url = "https://www.flipkart.com/search?q="+keyword

product_info = {}
product_nameList = []
product_priceList = []
product_ratingList = []

print("Connecting to Amazon and Flipkart")


def total_scrape():
    partial_dic = scrape(urlA, product_info, product_nameList,
                         product_priceList, product_ratingList)

    total_dic = scrape(url, partial_dic, product_nameList,
                       product_priceList, product_ratingList)
    return total_dic


final_dic = total_scrape()

print(final_dic)

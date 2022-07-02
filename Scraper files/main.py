

import pymongo
from MP_2 import scrape

connectionString = "mongodb+srv://admin:test@cluster0.5wvcy.mongodb.net/test"

if __name__ == '__main__':
    client = pymongo.MongoClient(connectionString)

    db = client['PriceComparison_DB']

    # Creating a collection
    collection = db.product_data

    product_info = {
        "product_img": "",
        "product_name": "",
        "product_info": "",
        "product_price": "",
        "product_rating": ""

    }

    # product_id = collection.insert_one(product_info).inserted_id
    # print(product_id)

    keyword = input("Enter product to search: ")
    keyword = keyword.replace(" ", "+")

    urlA = "https://www.amazon.in/s?k="+keyword
    url = "https://www.flipkart.com/search?q="+keyword
    scrape(urlA)

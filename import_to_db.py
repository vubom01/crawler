import json
import os

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1",
    database="poi_service"
)
mycursor = mydb.cursor()
sql = ("INSERT INTO pois (name, type, images, address, lat, lng, ref_id, "
       "rating, num_reviews, website, contact_phone, contact_email, status, source_type) "
       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 1, 1)")

path = "total"
dir_list = os.listdir(path)
res = []
for file_name in dir_list:
    f = open(f"{path}/{file_name}")
    data = json.load(f)
    res = res + data

print(len(res))

for item in res:
    type = 0
    if item["type"] == "attraction":
        type = 1
    if item["type"] == "hotel":
        type = 2
    if item["type"] == "restaurant":
        type = 3
    if item["address"] and len(item["address"]) > 500:
        item["address"] = None
    data = (item["name"], type, item.get("image"), item["address"], item["lat"], item["lng"], item["ref_id"],
            item["rating"], item["num_reviews"], item["website"], item["contact_phone"], item["contact_email"])
    mycursor.execute(sql, data)
    mydb.commit()
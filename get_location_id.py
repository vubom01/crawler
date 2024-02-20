import json
import os


def get_attraction_location_id(city):
    path = f"data_crawl/{city}/attractions"
    dir_list = os.listdir(path)

    location_ids = []
    for file_name in dir_list:
        try:
            f = open(f"{path}/{file_name}")
            data = json.load(f)
            ids = []
            for item in data:
                info = item.get("singleFlexCardContent")
                if info is None:
                    continue
                if info.get("saveId") is not None and info.get("saveId").get("id") is not None:
                    ids.append(int(info.get("saveId").get("id")))
            location_ids += ids
        except:
            print(f"err {city} attractions")

    return location_ids


def get_hotels_location_id(city):
    path = f"data_crawl/{city}/hotels"
    dir_list = os.listdir(path)

    location_ids = []
    for file_name in dir_list:
        try:
            f = open(f"{path}/{file_name}")
            data = json.load(f)
            ids = []
            for item in data:
                if item.get("locationId") is not None:
                    ids.append(int(item.get("locationId")))
            location_ids += ids
        except:
            print(f"err {city} hotels")

    return location_ids


def get_restaurants_location_id(city):
    path = f"data_crawl/{city}/restaurants"
    dir_list = os.listdir(path)

    location_ids = []
    for file_name in dir_list:
        try:
            f = open(f"{path}/{file_name}")
            data = json.load(f)
            ids = []
            info = []
            for item in data:
                if (item.get("data").get("response") is not None and
                        item.get("data").get("response").get("restaurants") is not None):
                    info = item.get("data").get("response").get("restaurants")
                    break

            for item in info:
                if item.get("locationId") is not None:
                    ids.append(int(item.get("locationId")))
            location_ids += ids
        except:
            print(f"err {city} restaurants")

    return location_ids

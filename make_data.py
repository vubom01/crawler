import json
import os

from constants import cities


def get_restaurants(c, location_dict):
    path = f"data_crawl/{c}/restaurants"
    dir_list = os.listdir(path)

    pois = []
    seen = set()

    for file_name in dir_list:
        f = open(f"{path}/{file_name}")
        response = json.load(f)
        data = []
        for item in response:
            if (type(item) != str and item.get("data").get("response") is not None and
                    item.get("data").get("response").get("restaurants") is not None):
                data = item.get("data").get("response").get("restaurants")
                break
        for item in data:
            location_id = item.get("locationId")
            if location_id not in seen:
                seen.add(location_id)
                if location_id in location_dict:
                    poi = location_dict[location_id]
                    if item.get("reviewSummary") is not None:
                        poi["rating"] = item.get("reviewSummary").get("rating")
                        poi["numberReviews"] = item.get("reviewSummary").get("count")
                    if item.get("thumbnail") is not None:
                        thumbnail = item.get("thumbnail")
                        if thumbnail.get("photo") is not None:
                            imageURL = thumbnail.get("photo").get("photoSizeDynamic").get("urlTemplate")
                            imageURL = imageURL.replace("w={width}&h={height}", "w=1000")
                            poi["image"] = imageURL
                    pois.append(poi)
    return pois


def get_hotels(c, location_dict):
    path = f"data_crawl/{c}/hotels"
    dir_list = os.listdir(path)

    pois = []
    seen = set()

    for file_name in dir_list:
        f = open(f"{path}/{file_name}")
        data = json.load(f)
        for item in data:
            location_id = item.get("locationId")
            if location_id not in seen:
                seen.add(location_id)
                if location_id in location_dict:
                    poi = location_dict[location_id]
                    if item.get("location") is not None and item.get("location").get("reviewSummary") is not None:
                        poi["rating"] = item.get("location").get("reviewSummary").get("rating")
                        poi["numberReviews"] = item.get("location").get("reviewSummary").get("count")

                    if item.get("location") is not None:
                        thumbnail = item.get("location").get("thumbnail")
                        if thumbnail is not None and thumbnail.get("photoSizeDynamic") is not None:
                            imageURL = thumbnail.get("photoSizeDynamic").get("urlTemplate")
                            imageURL = imageURL.replace("w={width}&h={height}", "w=1000")
                            poi["image"] = imageURL
                    pois.append(poi)
    return pois


def get_attractions(c, location_dict):
    path = f"data_crawl/{c}/attractions"
    dir_list = os.listdir(path)

    pois = []
    seen = set()

    for file_name in dir_list:
        f = open(f"{path}/{file_name}")
        data = json.load(f)
        for item in data:
            info = item.get("singleFlexCardContent")

            if info is None:
                continue

            location_id = int(info.get("saveId").get("id"))
            if location_id not in seen:
                seen.add(location_id)
                if location_id in location_dict:
                    poi = location_dict[location_id]
                    if info.get("bubbleRating") is not None:
                        poi["rating"] = info.get("bubbleRating").get("rating")
                        poi["numberReviews"] = info.get("bubbleRating").get("numberReviews").get("text")
                    if info.get("cardPhoto") is not None:
                        imageURL = info.get("cardPhoto").get("sizes").get("urlTemplate")
                        imageURL = imageURL.replace("w={width}&h={height}", "w=1000")
                        poi["image"] = imageURL
                    pois.append(poi)
    return pois


def import_to_db():
    for city in cities:
        path = f"data_crawl/{city}/detail"
        dir_list = os.listdir(path)

        seen = set()
        location_dict = {}
        pois = []

        for file_name in dir_list:
            f = open(f"{path}/{file_name}")
            response = json.load(f)

            if not isinstance(response, list):
                continue

            data = None
            if len(response) and response[0].get("data") and response[0].get("data").get("locations"):
                data = response[0].get("data").get("locations")

            if data is not None and len(data) and data[0] is not None:
                data = data[0]
                location_id = data["locationId"]
                if location_id not in seen:
                    seen.add(location_id)

                    poi_type = "restaurant"
                    if data.get("placeType") == "ACCOMMODATION":
                        poi_type = "hotel"
                    if data.get("placeType") == "ATTRACTION":
                        poi_type = "attraction"

                    address = None
                    if data.get("localizedStreetAddress") is not None:
                        address = data.get("localizedStreetAddress").get("fullAddress")

                    poi = {
                        'name': data.get("name"),
                        'type': poi_type,
                        'image': None,
                        'address': address,
                        'lat': data.get("latitude"),
                        'lng': data.get("longitude"),
                        'ref_id': location_id,
                        'rating': 0,
                        'num_reviews': 0,
                        'website': data.get('officialUrl'),
                        'contact_phone': data.get("telephone"),
                        'contact_email': data.get('email'),
                        'status': 1,
                        'source_type': 1,
                    }
                    location_dict[location_id] = poi

        print(len(location_dict))
        pois = pois + get_restaurants(city, location_dict)
        pois = pois + get_hotels(city, location_dict)
        pois = pois + get_attractions(city, location_dict)
        index = 0
        while index < len(pois):
            with open(f"total/{city}-{index}.json", "w") as outfile:
                outfile.write(json.dumps(pois[index:index + 10000]))
            index += 10000
        # with open(f"total/{city}.json", "w") as outfile:
        #     outfile.write(json.dumps(pois))
        print(f"DONE MAKE DATA {city}")


import_to_db()

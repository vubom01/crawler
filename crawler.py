import os
import threading

from crawl_data.crawl_attractions import crawl as crawl_attractions
from crawl_data.crawl_hotels import crawl as crawl_hotels
from crawl_data.crawl_restaurants import crawl as crawl_restaurants
from constants import cities, geo_ids
from crawl_data.crawl_restaurant_children import get_restaurant_children_ids
from detail import crawl_detail
from get_location_id import get_attraction_location_id, get_hotels_location_id, get_restaurants_location_id


def create_folder_in_data_crawl(city):
    path = os.path.join("data_crawl", city)
    os.makedirs(path, exist_ok=True)

    path = os.path.join(f"data_crawl/{city}", "attractions")
    os.makedirs(path, exist_ok=True)

    path = os.path.join(f"data_crawl/{city}", "restaurants")
    os.makedirs(path, exist_ok=True)

    path = os.path.join(f"data_crawl/{city}", "hotels")
    os.makedirs(path, exist_ok=True)

    path = os.path.join(f"data_crawl/{city}", "detail")
    os.makedirs(path, exist_ok=True)


def create_folder_in_logging(city):
    path = os.path.join("logging", city)
    os.makedirs(path, exist_ok=True)

    path = os.path.join(f"logging/{city}", "attractions")
    os.makedirs(path, exist_ok=True)

    path = os.path.join(f"logging/{city}", "restaurants")
    os.makedirs(path, exist_ok=True)

    path = os.path.join(f"logging/{city}", "hotels")
    os.makedirs(path, exist_ok=True)

    path = os.path.join(f"logging/{city}", "detail")
    os.makedirs(path, exist_ok=True)


def crawl_all_restaurants(geo_id, city):
    ids = get_restaurant_children_ids(geo_id, city)
    print(ids)
    for restaurant_id in ids:
        crawl_restaurants(int(restaurant_id), city)


def detail(city, location_ids):
    for location_id in location_ids:
        crawl_detail(city, location_id)


if __name__ == "__main__":
    for idx in range(len(cities)):
        city = cities[idx]
        geo_id = geo_ids[idx]
        create_folder_in_data_crawl(city)
        create_folder_in_logging(city)

        # t1 = threading.Thread(target=crawl_attractions, args=(geo_id, city))
        # t2 = threading.Thread(target=crawl_hotels, args=(geo_id, city))
        t3 = threading.Thread(target=crawl_all_restaurants, args=(geo_id, city))

        # t1.start()
        # t2.start()
        t3.start()

        # t1.join()
        # t2.join()
        t3.join()

        # location_ids_attractions = get_attraction_location_id(city)
        # location_ids_hotels = get_hotels_location_id(city)
        location_ids_restaurants = get_restaurants_location_id(city)

        # location_ids = location_ids_restaurants + location_ids_hotels + location_ids_attractions
        location_ids = location_ids_restaurants
        # location_ids = location_ids_hotels + location_ids_attractions

        location_ids = list(set(location_ids))

        total = len(location_ids)
        print(f"total {city} = {total}")
        print("START CRAWL DETAIL {city}")
        location_ids1 = location_ids[:total // 2]
        location_ids2 = location_ids[total // 2:]

        t11 = threading.Thread(target=detail, args=(city, location_ids1))
        t12 = threading.Thread(target=detail, args=(city, location_ids2))

        t11.start()
        t12.start()

        t11.join()
        t12.join()

        print(f"DONE {city}")

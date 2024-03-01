import datetime
import json
import os
import sys
import time

import requests

from constants import cities

url = "https://www.tripadvisor.com.vn/data/graphql/ids"


def get_detail_payload(location_id):
    request = [
        {
            "variables": {
                "locationIds": [
                    22138473
                ]
            },
            "query": "6c75c91440247cf1",
            "extensions": {
                "preRegisteredQueryId": "6c75c91440247cf1"
            }
        }
    ]
    request[0]["variables"]["locationIds"] = [location_id]
    return json.dumps(request)


headers = {
    'authority': 'www.tripadvisor.com.vn',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'cookie': 'TASameSite=1; TAUnique=%1%enc%3A5P%2B2nzkmiCPVbaARsw%2BWMUb%2FeeFk7hQlwJb0MdWLwuM%3D; TASSK=enc%3AAMl8vzykg1%2BedILlGaIVIPw5TM1%2B3v8x2ONJwls0Te5cjWDJ8s2mBMq64%2BjP9xPX3kSUtVH0lOW3%2FD%2FlkwLwH5c8q3f1Y6g7CL1%2FwrL886Wd9xWttfJfCLOeceHm6slyJw%3D%3D; VRMCID=%1%V1*id.21047*llp.%2F-a_gclid%5C.Cj0KCQjwpc__2D__oBhCGARIsAH6ote9X__2D__m6C9f__5F__A5F1K8kWhT6gg__2D__8XogqOJcdNMwi4FdFnJxetqONJLOw4aAgcTEALw__5F__wcB-m21047-a_supac%5C.4188770428-a_supag%5C.13190924659-a_supai%5C.603985187687-a_supbk%5C.1-a_supcm%5C.193220179-a_supdv%5C.c-a_supli%5C.-a_suplp%5C.1028580-a_supnt%5C.g-a_supti%5C.kwd__2D__119671122*e.1696484938987; TATrkConsent=eyJvdXQiOiIiLCJpbiI6IkFMTCJ9; _ga=GA1.1.2010389825.1695880148; TART=%1%enc%3A1W2gEbMPljFa5TuLUTjWgxQEB7GEaROCKNftcP4W8E8EwVf2KAPCNDV%2Fyv5R7jJ%2BNox8JbUSTxk%3D; ServerPool=B; PMC=V2*MS.82*MD.20230928*LD.20231005; TASID=4A4F02904148866D54CAAABFD35C9B8D; TATravelInfo=V2*AY.2023*AM.10*AD.15*DY.2023*DM.10*DD.16*A.1*MG.-1*HP.2*FL.3*DSM.1696488408841*AZ.1*RS.1; TAReturnTo=%1%%2FHotel_Review-g293924-d12799616-Reviews-InterContinental_Hanoi_Landmark72-Hanoi.html%26spAttributionToken%3DMTg0OTAxODg; ab.storage.sessionId.6e55efa5-e689-47c3-a55b-e6d7515a6c5d=%7B%22g%22%3A%22ad860163-23ef-cc68-b178-ce7e9bc64e12%22%2C%22e%22%3A1696496852662%2C%22c%22%3A1696496792663%2C%22l%22%3A1696496792663%7D; ab.storage.deviceId.6e55efa5-e689-47c3-a55b-e6d7515a6c5d=%7B%22g%22%3A%22730caa4d-b678-940a-33f0-21ed0d1fc711%22%2C%22c%22%3A1695880174531%2C%22l%22%3A1696496792664%7D; TADCID=VifuI1-ZyQQHKxkoABQCCKy0j55CTpGVsECjuwJMq3iq8XGivh5IhYzwc68UwvmtzqCxHRIbhYkrj8flO0Jb8y2BO3bsmXtFOk4; TAUD=LA-1695880138642-1*RDD-1-2023_09_28*ARC-532572775*HDD-533659856-2023_10_15.2023_10_16*HD-617557673-2023_10_15.2023_10_16*VRD-617557674-2023_10_15.2023_10_16*G-617557675-1.1.-1.*VRG-617557676-1.0*LD-621647224-2023.10.15.2023.10.16*LG-621647227-1.1.T.*ARDD-621647228-2023_10_15.2023_10_16; PAC=AK-GS2htqm9ISiU8Md-YkoFpdSLjnyUTK9eHVcGdFvE8O4RXzeXwXvQEcW8ElHTD_rdGb-Mu9ymeffgJgpul4RMIrEsnuXwF5eCJ6KLL8WfNvpRKrEvwGN_7wFh-JBiM0NwDkei7DCSFhNOLeZm38R4S52LVQhEQr2PuvBUEXtkdqgbOHUd2TZtvroGcEOJKC_TysoniWYgM-NIkiehkVOR_C3FaKDnztxIRCPFRcm30; TASession=V2ID.4A4F02904148866D54CAAABFD35C9B8D*SQ.233*LS.Attractions*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*LF.vi*FA.1*DF.0*TRA.true*LD.293924*EAU._; _ga_QX0Q50ZC9P=GS1.1.1696488313.5.1.1696503968.60.0.0; __vt=I3C-fa95APCkrxeFABQCCQPEFUluRFmojcP0P3EgGiiI50-dgS86Ch_12rRSGyiUmN_0o_4_xMd--wZeQVQPGLgX7Ddr8wwQLrAAQNam3M6zRmuczJbvERk0kJscADpRgksfeMMs5LVmwykdKYb0Lttyyw; datadome=4EsB71yQXJTsCtK20fTHQmoANtPkxs1UKHmFMzN8VENpyPXWuMaWighD5wSZwOavceBMqv8hKCUcin0EoyP_oUiCSg9m_kixqVmIKsuQn79DYUTYcSDDYbD-tFHVFgBW; SRT=:%1%enc%3A1W2gEbMPljFa5TuLUTjWgxQEB7GEaROCKNftcP4W8E8EwVf2KAPCNDV%2Fyv5R7jJ%2BNox8JbUSTxk%3D; __vt=pPJnW7Sdh9ebcgFAABQCCQPEFUluRFmojcP0P3EgGiiIu3uHiiHrs76piaJ4lBBgRtJ7eZ3I2Hd1Mj3w4ZUGhAjCHGOHwOSVzxDP-fWWoMYn5qpLdDhNla18edhVgQAiIn1Yv3B7LLdmqZ9rLNR9BHFQTw',
    'origin': 'https://www.tripadvisor.com.vn',
    'referer': 'https://www.tripadvisor.com.vn/Attractions-g293924-Activities-oa60-Hanoi.html',
    'sec-ch-device-memory': '8',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-full-version-list': '"Chromium";v="116.0.5845.187", "Not)A;Brand";v="24.0.0.0", "Google Chrome";v="116.0.5845.187"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'same-origin',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'x-requested-by': 'c3f5174c4155236d2095919106142c80353489546ed30526ec398131dbf13944'
}


def crawl_detail(city, location_id):
    files = []
    data_local_path = f"data_crawl/{city}/detail"
    dir_list = os.listdir(data_local_path)
    for file_name in dir_list:
        files.append(file_name)

    try:
        if f"{location_id}.json" in files:
            print(f"{city}: detail {location_id} exist")
        else:
            payload = get_detail_payload(location_id)
            response = requests.request("POST", url, headers=headers, data=payload)
            data = response.json()
            with open(f"data_crawl/{city}/detail/{location_id}.json", "w") as outfile:
                outfile.write(json.dumps(data))
            print(f"{city}: detail {location_id} success")
    except Exception as e:
        log = {
            "location_id": location_id,
            "error": str(e),
        }

        with open(f"logging/{city}/detail/{location_id}.json", "w") as outfile:
            outfile.write(json.dumps(log))
        print(f"crawl location_id = {location_id} error")





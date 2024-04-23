import os
import json
import requests

url = "https://www.tripadvisor.com/data/graphql/ids"


def get_payload(geo_id, offset):
    request = [
        {
            "variables": {
                "geoId": 294226,
                "filters": {
                    "minRating": None,
                    "neighborhoodsOrNear": None,
                    "priceRange": None,
                    "amenities": None,
                    "brands": None,
                    "classes": None,
                    "styles": None,
                    "hoteltypes": None,
                    "categories": None,
                    "anyTags": None
                },
                "offset": 30,
                "limit": 30,
                "sort": "BEST_VALUE",
                "clientType": "DESKTOP",
                "viewType": "LIST",
                "productId": "Hotels",
                "pageviewId": "LIT@Anag2EKuR4ufAW0u4Qwo",
                "sessionId": "954B6B551D48A48B51AFB9B3FBE90F6E",
                "amenityLimit": 5,
                "userEngagedFilters": False
            },
            "extensions": {
                "preRegisteredQueryId": "388ac7e8c6deb42f"
            }
        }
    ]
    request[0]["variables"]["offset"] = offset
    request[0]["variables"]["geoId"] = geo_id
    return json.dumps(request)


headers = {
    'authority': 'www.tripadvisor.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'cookie': 'TADCID=qnUeuHIA2kfIfoEBABQCCKy0j55CTpGVsECjuwJMq3ikKYOuug9TQd-cxWZyu3vOGSGhLWCSYLdU9kYsVuB5Clj-iSQHaerdvaw; TASameSite=1; TAUnique=%1%enc%3AWtOGVbhzXZrVbaARsw%2BWMbJ4l0mTvdZNTTydHRRNQOU%3D; TASSK=enc%3AANBOHkqPGGj7fnDBuP8saJCJ5C2jH0M6SzXIPtdzmXbdUCHRpIr%2FBee2EWGPRBcht%2Bs31o8XNzSz2HxZyNE1iLUbYB5au2vIfkMgCE0ZB0lrR7tcTrVtyuuKddgjQCYy0A%3D%3D; ServerPool=C; PMC=V2*MS.54*MD.20231004*LD.20231004; TATrkConsent=eyJvdXQiOiIiLCJpbiI6IkFMTCJ9; _pbjs_userid_consent_data=3524755945110770; _li_dcdm_c=.tripadvisor.com.vn; _lc2_fpi=28c87295fd99--01hbwg1k6mpjgaskwrvcw0gs24; pbjs_sharedId=0819579f-2627-49f2-92ae-5d24daf27f27; _ga=GA1.1.1474231513.1696394694; _lr_sampling_rate=100; __li_idex_cache_e30=%7B%7D; pbjs_li_nonid=%7B%7D; G_AUTH2_MIGRATION=informational; AMZN-Token=v2FweIBVQjB0eDFoM0UzVGZmZDltSzNHMnNjM3Z3N2NkVFF1cHlLdFV1ZWFRejdBSUIxU25PdWNqR1EveW1zUUpTUGZZL1JQNHplZ3BXQkFvR2NoZGRZOCtuTlFJdlVqT1Robnc0dDlpdnIyM25HN2oxai9kWmEvNFJLN0VKUFN0NDhaNmJrdgFiaXZ4IFBEOGc3Nys5VSsrL3ZlKy92WFplNzcrOTc3Kzk3Nys5/w==; _lr_env_src_ats=false; TATravelInfo=V2*AY.2023*AM.10*AD.15*DY.2023*DM.10*DD.16*A.2*MG.-1*HP.2*FL.3*DSM.1696402348839*RS.1; TART=%1%enc%3Ats5cxHjqP8WmeSKTPARNmZV%2B%2FzgfDX8%2BFFDto8V%2BRVnPp6GqM770UxIYhPsxu9m6i68p65Z0IW4%3D; PAC=AGPcC61q8Wm42JVFSglrrkassrNnx2Poo9rx4SPjbxjKfVv3cl2zrBdYPsESgv7E8jXoIr5QIy4vVtBz2Fk34Yg1dV2z63N9bQDVt8RT3SwkipcqjQnR05vOJVb3eGb00PG-kE0VgyjJBW4rP6cVYWPvWqOKLhCMxLYA1ZhCQpIPZvQhWbEFeS9GzpXXBTunCdnL0S_Amy0WCza08W8TqcVvIaFR2QO5JBG08CiEgRi14GaNxXWfLoRNQOsZGFgTK_B4DqLO0DzFuPhjCq9TwZ4%3D; TASID=546749106A5A49F684BD583D2F0AC1E7; _lr_retry_request=true; TAReturnTo=%1%%2FHotel_Review-g25197573-d25266275-Reviews-Wink_Hotel_Danang_Riverside-An_Hai_Son_Tra_Peninsula_Da_Nang.html; roybatty=TNI1625!AAVzRL%2B99tIdrA6LgqGYgqQNpgqcJq%2FqYm7zHgTVIceg0GRRGDG7Sbef%2FriekLQ%2F2QvIv7DM2fBm72130Co6KxXwAFXcU5gSoLSM0uOz9q6GrljT%2FT%2Fjd4aj%2FF%2Bswmj6WiCK%2FUBxJ87trgoFkLihSFNQJ1BYgRACH8AjWf4WRi%2Bd%2C1; ab.storage.sessionId.6e55efa5-e689-47c3-a55b-e6d7515a6c5d=%7B%22g%22%3A%22df849cd7-6ffe-6a17-bfc6-5a1f54f75309%22%2C%22e%22%3A1696406219829%2C%22c%22%3A1696406159839%2C%22l%22%3A1696406159839%7D; ab.storage.deviceId.6e55efa5-e689-47c3-a55b-e6d7515a6c5d=%7B%22g%22%3A%22a701c25b-7123-1fa4-f457-4c448d3ca610%22%2C%22c%22%3A1696402355598%2C%22l%22%3A1696406159846%7D; __vt=ulrQPbGmNBUyKV5LABQCCQPEFUluRFmojcP0P3EgGiiCjcMQfClo17vMB2QjjSzLXkqdarD4c8-_z8G7Ssy8dx7l0-QgkCUh_XOfeCXzwbEu0PbBQqurk7hRc6Ca9kD7xi9sDPjueJGAhokp5xwM8Ids4kKA9oFEQJdNWbKn2uXXPkgOn8gXNJzDlKiOSV4CSFoBkd1oO-PRAg; SRT=TART_SYNC; __gads=ID=3eb46b4d5e85d9a1:T=1696394695:RT=1696406451:S=ALNI_MYuVfQJzkh_lmLBtVGi70bvFF5Caw; __gpi=UID=00000c5723458136:T=1696394695:RT=1696406451:S=ALNI_MYB4Qq329j0t_Blnv5Z-ZN54q4uvA; TAUD=LA-1696394700160-1*RDD-1-2023_10_04*ARC-2904*HDD-7648525-2023_10_15.2023_10_16*LD-11758924-2023.10.15.2023.10.16*LG-11758926-2.1.F.; datadome=41xUuTTXyAjNTvE8ZR~rxxTz2qfGzvl7aP5tIeHITWhxi1P-CKrTAZP~dq44_Sd~YuU3mxVSvHy48477HrPaHXGND758OPFvh~VEUu_eWrtneHiWouR5SoHM2w8601TG; _ga_QX0Q50ZC9P=GS1.1.1696405075.3.1.1696406463.46.0.0; TASession=%1%V2ID.546749106A5A49F684BD583D2F0AC1E7*SQ.92*PR.40185%7C*LS.Hotels*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*LF.vi*FA.1*DF.0*TRA.true*LD.298085*EAU._; _dd_s=logs=1&id=d00f5b77-06d2-42bf-ae2f-fd9231266c17&created=1696402290579&expire=1696407365906; __vt=ODQXz846hZLwXWf0ABQCCQPEFUluRFmojcP0P3EgGiiHILBNotjCGdYFTouFcIF0fgV1B-Zyntk-TLJrs4Eq2Z8rAc3dmm0Jo0jt7enI8zsRTJrUp4ulrVoezuTbK09Kl7knivOiCh2rR5NyUl9FZ_KGTjj_BHk0QiIt0AbvTSQS_iYO6aeHIBkA8M5mW9DkrBklM8bGf3bueA',
    'origin': 'https://www.tripadvisor.com',
    'sec-ch-device-memory': '8',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="117.0.5938.132", "Not;A=Brand";v="8.0.0.0", "Chromium";v="117.0.5938.132"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'same-origin',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'x-requested-by': '057504f7e4196d77f891b69fc6e59f10e172fb3d8ae0f125b2153cf6bee8f69a'
}


def crawl(geo_id, city):
    files = []
    data_local_path = f"data_crawl/{city}/hotels"
    dir_list = os.listdir(data_local_path)
    for file_name in dir_list:
        files.append(file_name)

    offset = 0

    while True:
        payload = get_payload(geo_id, offset)

        try:
            if f"page{offset}.json" in files:
                print(f"hotels: {offset} exist")
            else:
                response = requests.request("POST", url, headers=headers, data=payload)
                data = response.json()[0].get('data').get('list').get('results')
                with open(f"data_crawl/{city}/hotels/page{offset}.json", "w") as outfile:
                    outfile.write(json.dumps(data))
                print(f"hotels: crawl offset = {offset} success")
                if len(data) == 0:
                    break
        except Exception as e:
            log = {
                "payload": payload,
                "offset": offset,
                "error": str(e),
            }

            with open(f"logging/{city}/hotels/page{offset}.json", "w") as outfile:
                outfile.write(json.dumps(log))
            print(f"hotels: crawl offset = {offset} error")
        finally:
            offset += 30

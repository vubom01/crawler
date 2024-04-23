import os

import requests
import json

url = "https://www.tripadvisor.com/data/graphql/ids"


def get_payload(geo_id, offset):
    request = [
        {
            "variables": {
                "request": {
                    "routeParameters": {
                        "geoId": 294226,
                        "pagee": "0",
                        "contentType": "attraction",
                        "webVariant": "AttractionsFusion",
                        "filters": [],
                    },
                },
                "mapSurface": False,
                "debug": False,
                "polling": False
            },
            "extensions": {
                "preRegisteredQueryId": "42974f26ab4c21f7"
            }
        }
    ]

    request[0]["variables"]["request"]["routeParameters"]["pagee"] = f"""{offset}"""
    request[0]["variables"]["request"]["routeParameters"]["geoId"] = geo_id
    return json.dumps(request)


headers = {
    'authority': 'www.tripadvisor.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'cookie': 'TASameSite=1; TAUnique=%1%enc%3A%2FOacsCHGmtSUsjVVDX5enfsyu%2ByO%2FqyPIbVsNi1qz%2Bd8fL%2BUqsUlcRcNC14G%2FYGrNox8JbUSTxk%3D; TASSK=enc%3AAOfGfXyw65OD9vE%2Bf%2Bj%2FV5qKdrZIiuVH7nCAbHBq3RdCTe40EergFSudo8u%2F%2FO1n1RrLoizcsgUGJd7b2NJmtD5Tcz%2BpKGH46dYkyQhMpRz10tc%2F9PTO1Idko2tJTn3fgQ%3D%3D; VRMCID=%1%V1*id.21047*llp.%2F-a_gclid%5C.Cj0KCQiAyeWrBhDDARIsAGP1mWSzjk916pkAbOFKSgKWbLnlgA__2D__J__5F__p7mZl8ctNHRE6q7mQiXBYQisaQaAl9cEALw__5F__wcB-m21047-a_supac%5C.4188770428-a_supag%5C.13190924659-a_supai%5C.671736848550-a_supbk%5C.1-a_supcm%5C.193220179-a_supdv%5C.c-a_supli%5C.-a_suplp%5C.1028580-a_supnt%5C.g-a_supti%5C.kwd__2D__119671122*e.1703140709392; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*DSM.1702536091918*RS.1; TASID=6E6A7DF85F1634FDB2AD45076E473107; TADCID=N418c8Kks0MbDe3kABQCCKy0j55CTpGVsECjuwJMq3qqfX1LYxwBiI1Dtkuhx9Pg_IVUOwtf-XuhM5pRLQ_C6t_RqznCdu0OdR8; PAC=AENH7YZqyBXGfn7yz-fOAtKO-swkd0Qes6x5TWKoAGj_0gJZgpDRaeAs1j4-i8PcJVeYDnrwmUDUzT10ec3HG_bf1exuhr-eKVMiphQO_9bQC0ZRU_VrOPCjhYSAM01LKAETmidcT2bxr2kTaeWbEB4sKD3l8_YpPW8B9IVObNl3wH1Ux7KmgB42Y8oN4R8hxIjutGa79toEHF2X76QuHDhQQBC21Jh-eHHkFYq2sVtHh7SEPJ3QZIrfEJ6pWi4b3IwvUVgFNiOQfdiE1Ou1T_UW5nUS9cvv9oCgrY5FtVyq-h-lUj3pXovubeK3VBIzD3YdXfOIiDe2ocKEqlqFDfLexwjbq1CwiiX1Oa_YnhreXS31LFLaG7OZfG9jssm1JDaNFuBqcLj2nFTnm5l7xltpxBfMjEPMwwQrVExmYe8RUt2v8jH3ama7kgZ-o7fJkM6WfyhxXtR8ayeANxv_6-RyynX1ntxpGRmiwT4P6bVjlfjFBZ-abfeQn2m4RvsIxaTrgDyJyj34BAlRXKbl6ELfuo5yf1slW_1UcW2Nms9r5bSAbwVoD95SP3u2bGSGLA%3D%3D; ServerPool=C; PMC=V2*MS.100*MD.20231122*LD.20240104; TART=%1%enc%3A1W2gEbMPljE0GW%2FJQSTgwaFYPr%2FgTFjGgMEq3Eihoi%2BMmfotxeiIdJzLfT5ymwfcNox8JbUSTxk%3D; TAAUTHEAT=Ns_sa3OpimjtOfmFABQCobW21V9oR1-Dg22GNw6BiDqBfUPjaBslJOsxGgoMgT3QtQD2xtBcN0E1JDoUDdME0Am-mZFUIiznzpz6WZAbTfmffebIc5HQeNXrrgqqr16p2jwR6il4B56TViBnhp5uZq1TQqWzqkXNac1ypHy9CzFZQO30xhoWD5PGvdvQeDEy9vuZA9vK03VA3rL0SR7dFKZiHiwSynkQ4mBrdN4R; SRT=TART_SYNC; __vt=MbZRHAHXUZ7ZZlXBABQCCQPEFUluRFmojcP0P3EgGiqIQZso4Y51vgqrpbHCYsEANWFYvtEfXhQg2LIIrvZdTjLsF1m_Buh0ijHl_TGVbnmiuqbpiDu_48WTDqStdDm9gZTisWvneCldeiavnhZpuQIQOfr-vp8xQzaW04sAwb4npO3Tw0vBiWLWk7GoDq1KTxf-8Mfbn5zd2pI; TATrkConsent=eyJvdXQiOiJBRFYsU09DSUFMX01FRElBIiwiaW4iOiJBTkEsRlVOQ1RJT05BTCJ9; TAReturnTo=%1%%2FRestaurants-g28926-oa20-California.html; roybatty=TNI1625!APW3%2B5WKT%2BOG2vX7Btt%2BuLCO634ZdlMkLp0knISCWOCN9%2FqTwRahe98LZV3pg%2BDBDH%2BS9DjQu4AxIV4S4ogLT1pWSmO7WqmLZWaLnxemYE%2BsAFmeV%2BhlYp7%2BIaH6Tg8prDF94yKEwOvTu5X6JdTJg5lgGK7UzyzkB%2BxL7zgLMSH7M4XqBp%2FUQhBK73C1Em9u5g%3D%3D%2C1; TAUD=LA-1700639443508-1*RDD-1-2023_11_22*HDD-1896648295-2023_12_24.2023_12_25*ARC-3719202219*LG-3719253281-2.1.F.*LD-3719253282-.....; TASession=V2ID.6E6A7DF85F1634FDB2AD45076E473107*SQ.88*LS.Attractions*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.4743823F4BBA15E7757DBEAD63318E39*FA.1*DF.0*TRA.true*LD.32724*EAU.4; __gads=ID=de28916d3343f924:T=1700639446:RT=1704358964:S=ALNI_MZXUaS1G9Y-EwGChaE56qnzRhX88Q; __gpi=UID=00000c93f8f8e62b:T=1700639446:RT=1704358964:S=ALNI_MYvmINZPmdXI2KX7Dzv3vE4TeqQuA; datadome=I5~8BIiPmwOoduu9sDXtqt73gIku~U57SOEEIoAPLcptz6gnPw037Xpl9zTQi06lR54M0_2CQMcOiHNmzrJ3E4JiO8vAZVIcAkbBq73YLTK8y_yZhP2W9h5V~Aw64lbX; TAUnique=%1%enc%3AX%2FiE4CdbSizoCEVTOyX2USlBHXRcfYqsp%2Fct9omJ6QyggluDXKQh3wsJvUuiZBwrFZ2%2Bd7y9LSs%3D; TADCID=CAITa1kXKeenGwBtABQCCKy0j55CTpGVsECjuwJMq3jopD2BajvD1N_1Ck373zFgnvOPCUqBaxqdn7mBHERzJ2pWKugYfR60mEY; TASameSite=1',
    'dnt': '1',
    'origin': 'https://www.tripadvisor.com',
    'sec-ch-device-memory': '8',
    'sec-ch-ua': '"Chromium";v="117", "Not;A=Brand";v="8"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-full-version-list': '"Chromium";v="117.0.5938.157", "Not;A=Brand";v="8.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'same-origin',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'x-requested-by': 'aed06af1cf560d742a4081756d44a52b0a8665724a48b7ad3a2c83f963e3a0ff'
}


def crawl(geo_id, city):
    files = []
    data_local_path = f"data_crawl/{city}/attractions"
    dir_list = os.listdir(data_local_path)
    for file_name in dir_list:
        files.append(file_name)

    offset = 0

    while True:
        payload = get_payload(geo_id, offset)

        try:
            if f"page{offset}.json" in files:
                print(f"attractions: {offset} exist")
            else:
                response = requests.request("POST", url, headers=headers, data=payload)
                data = response.json()[0].get("data").get("Result")[0].get("sections")
                with open(f"data_crawl/{city}/attractions/page{offset}.json", "w") as outfile:
                    outfile.write(json.dumps(data))
                print(f"attractions: crawl offset = {offset} success")
                is_break = True
                for item in data:
                    info = item.get("singleFlexCardContent")
                    if info is not None and info.get("saveId") is not None:
                        is_break = False
                if is_break:
                    break
        except Exception as e:
            log = {
                "payload": payload,
                "offset": offset,
                "error": e,
            }

            with open(f"logging/{city}/attractions/page{offset}.json", "w") as outfile:
                outfile.write(json.dumps(log))
            print(f"attractions: crawl offset = {offset} error")
        finally:
            offset += 30

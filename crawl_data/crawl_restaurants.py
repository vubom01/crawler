import json
import os

import requests

url = "https://www.tripadvisor.com.vn/data/graphql/ids"


def get_payload(geo_id, offset):
    request = [
        {
            "variables": {
                "limit": 30,
                "racRequest": None,
                "route": {
                    "page": "Restaurants",
                    "params": {
                        "geoId": 34047,
                        "offset": "30"
                    }
                },
                "additionalSelections": [
                    {
                        "facet": "ESTABLISHMENT_TYPES",
                        "selections": [
                            "10591"
                        ]
                    }
                ]
            },
            "extensions": {
                "preRegisteredQueryId": "1907e3a744fd482a"
            }
        }
    ]
    request[0]["variables"]["route"]["params"]["geoId"] = geo_id
    request[0]["variables"]["route"]["params"]["offset"] = f"{offset}"

    return json.dumps(request)


headers = {
    'authority': 'www.tripadvisor.com.vn',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'cookie': 'TASameSite=1; TAUnique=%1%enc%3A%2FOacsCHGmtSUsjVVDX5enfsyu%2ByO%2FqyPIbVsNi1qz%2Bd8fL%2BUqsUlcRcNC14G%2FYGrNox8JbUSTxk%3D; TASSK=enc%3AAOfGfXyw65OD9vE%2Bf%2Bj%2FV5qKdrZIiuVH7nCAbHBq3RdCTe40EergFSudo8u%2F%2FO1n1RrLoizcsgUGJd7b2NJmtD5Tcz%2BpKGH46dYkyQhMpRz10tc%2F9PTO1Idko2tJTn3fgQ%3D%3D; VRMCID=%1%V1*id.21047*llp.%2F-a_gclid%5C.Cj0KCQiAyeWrBhDDARIsAGP1mWSzjk916pkAbOFKSgKWbLnlgA__2D__J__5F__p7mZl8ctNHRE6q7mQiXBYQisaQaAl9cEALw__5F__wcB-m21047-a_supac%5C.4188770428-a_supag%5C.13190924659-a_supai%5C.671736848550-a_supbk%5C.1-a_supcm%5C.193220179-a_supdv%5C.c-a_supli%5C.-a_suplp%5C.1028580-a_supnt%5C.g-a_supti%5C.kwd__2D__119671122*e.1703140709392; TATrkConsent=eyJvdXQiOiJBRFYsU09DSUFMX01FRElBIiwiaW4iOiJBTkEsRlVOQ1RJT05BTCJ9; TART=%1%enc%3AcLxO8gaW0J5lYxyD1%2FJuyAzputVtHAwJH6yBNCfVqAg%2BlQWJZ%2BMRejCOXldokDPS6BCWM1oYsLg%3D; TATravelInfo=V2*AY.2024*AM.2*AD.11*DY.2024*DM.2*DD.12*A.2*MG.-1*HP.2*FL.3*DSM.1706768267403*RS.1; TADCID=PXNJI0ac-Itq55z3ABQCmq6heh9ZSU2yA8SXn9Wv5HtddYbKk-tGMbrzTHku8BDOGQbqO4RVa-GeqyRDkkRTk5Gmp08C2p5Ufg0; TAAUTHEAT=k-Tfexny2LFBplaAABQCNrrFLZA9QSOijcELs1dvVzs0dUCohmtSECJQZRSpxFlh1zmVWU38IgxwISPH0oK0C7bxTwkmC1_i0rGx_bhLbkZNejzGUGORUt4E3j_X3l3MM1OOE_yKn6pbqxTAPwk4YdmEfyhJxNPkywUTfF2MQuXvgKSm3oq6L2DCzq8WpY9ELZq-B14AXGAdgxzxcYpR3sIQIDlb4L6k2QFxfTJ0; ServerPool=C; TASID=129D313E35344EAA9B95B1923E76D12E; PAC=AIIcigJq9ivhfX1EPlM6isqEBjH6pMgbz2TnDMoGTti1cMpziKl69PPAkB6ZGJVSTi_mOZ5DdKKFH5uhlTbsJJ-fJEhdJY14JEvPMeGp9f2uJXFy5Tw8hZUvpt70JXXsQyvMMkpFL_WlWUUflYMZR-WxzML6tcwBzpgMQDo21KPe; PMC=V2*MS.40*MD.20240122*LD.20240205; SRT=TART_SYNC; __vt=E3PFs5S8zAPonKEWABQCwRB1grfcRZKTnW7buAoPsSs748HSqGPfs7hkCUi7qAfLdYUbBGOuJqVwdaz5cMaOgN6Tu0q7OyrPnyMMcz8yVZ_y-PNIPAhYTf-6HGJ89xZsjDsow3uWwML2B5Y2DLZeLaHlFMPcnKH-Rm18eiJIVY98Kyrp1S5M_lGqrReipWj_JU8V8WtoxaS_8DA; __gads=ID=de28916d3343f924:T=1700639446:RT=1707117527:S=ALNI_MZXUaS1G9Y-EwGChaE56qnzRhX88Q; __gpi=UID=00000c93f8f8e62b:T=1700639446:RT=1707117527:S=ALNI_MYvmINZPmdXI2KX7Dzv3vE4TeqQuA; __eoi=ID=d924c91a8bc9c535:T=1706759225:RT=1707117527:S=AA-AfjYtsiqdQ9erETJnpVqBTqK7; TAReturnTo=%1%%2FRestaurants-g28929-oa40-Delaware.html; roybatty=TNI1625!AAvap0lHhSCP4g2mbYgUkZwD5eiJEZtUaOjtJsXsWoH8WoII%2BmE16SssM4gpclzyL9btAFUwnyHBhRKRx4hOAA6puU3Q%2FhHc%2FigtoA7deFAUL3Y7pL2cx4h8%2Bby5oGOOHJJlRUw1%2FrLHgHmUqzb%2FdfJNwh2rEW4Bo28xODqjq3s3rmpMK5Uvw6WRCjoEMrGNRw%3D%3D%2C1; TAUD=RDD-1705631942103-2024_01_18*FO-360758194-HAN*FD-360758195-LAX*LA-360758196-1*RTD-360758203-2024_02_06.2024_02_13*FT-360758204-1.0.CS0*ARDD-365438211-2024_02_06.2024_02_13*HDD-1136325194-2024_02_11.2024_02_12*ARC-1231114584*LG-1485652916-2.1.F.*LD-1485652917-.....; TASession=V2ID.129D313E35344EAA9B95B1923E76D12E*SQ.77*LS.Restaurants*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.4743823F4BBA15E7757DBEAD63318E39*FA.1*DF.0*TRA.true*LD.34047*EAU.4; datadome=m7KYLeMR0Td5XNSf4DWmLISG18UDCax4sPy5q24vyUVfzPuF_KRyHEOhx_fUBN4gW2XTP3N8vzkR50I1mSTjKELvmHKtSGlh6EMoeO1KVlYXfnAdJzlGiEs1a~mvXK08; CM=%1%PremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CRestAds%2FRPers%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7Cpv%2C0%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CCrisisSess%2C%2C-1%7CUVOwnersSess%2C%2C-1%7CRestPremRSess%2C%2C-1%7CRepTarMCSess%2C%2C-1%7CCCSess%2C%2C-1%7CCYLSess%2C%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CRestAdsPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7CTSMCPers%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CTADORSess%2C%2C-1%7CAdsRetPers%2C%2C-1%7CListMCSess%2C%2C-1%7CTARSWBPers%2C%2C-1%7CSPMCSess%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7Cmdpers%2C1%2C1707719066%7CRBAPers%2C%2C-1%7CRestAds%2FRSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7CRestPremRPers%2C%2C-1%7CRevHubRMPers%2C%2C-1%7CUVOwnersPers%2C%2C-1%7Csh%2CRuleBasedPopup%2C1707200666%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCrisisPers%2C%2C-1%7CCYLPers%2C%2C-1%7CCCPers%2C%2C-1%7CRepTarMCPers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CTSMCSess%2C%2C-1%7CSPMCPers%2C%2C-1%7CRevHubRMSess%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CAdsRetSess%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CTADORPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CTARSWBSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRestAdsSess%2C%2C-1%7CRBASess%2C%2C-1%7CSPORPers%2C%2C-1%7Cperssticker%2C%2C-1%7CListMCPers%2C%2C-1%7Cmdsess%2C-1%2C-1%7C; ServerPool=C; TAReturnTo=%1%%2FRestaurants-g28929-oa20-Delaware.html; TASession=V2ID.A0C42C1BB987498594010F9BAF171150*SQ.7*LS.Restaurants*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.4743823F4BBA15E7757DBEAD63318E39*FA.1*DF.0*RT.0*TRA.true*LD.28929; TATravelInfo=V2*AY.2024*AM.2*AD.6*DY.2024*DM.2*DD.13*A.2*MG.-1*HP.2*FL.3*DSM.1706864358602*RS.1; TAUD=LA-1707104211277-1*RDD-1-2024_02_02*LG-10055531-2.1.F.*LD-10055532-.....; TAUnique=%1%enc%3AX%2FiE4CdbSizoCEVTOyX2USlBHXRcfYqsp%2Fct9omJ6QyggluDXKQh3wsJvUuiZBwrFZ2%2Bd7y9LSs%3D; datadome=P2DFILhbvx6Y49K99QrdSAs9GmEU0eOffJEw~eTpemWgPVGZTOdUvt_01kHQ3LNbQEnKo6SV83~k_KaY_ryRaxk3KTkNG~NR3_Ngow_VwJ0v3L2Bb~3_qmzHFS0p_plw; PAC=APzy7tYrOXDcyFrmCuCtIivBZDzR_nXzCTrFxGw2u5sFNKDoqfhvQwl9HmAZQmJRsW0Wx6R-TghVIFx8Ru0fDwSFReNfsgcZz_eW3hOEpcAiLxL5tWH5tDAsnNpWS-iceryppk92WXugv2DvEXm7pcLsotbPK7AuguauE8No9ePE; PMC=V2*MS.69*MD.20240118*LD.20240205; TAAUTHEAT=1BGvonqBCq9-6FnMABQCNrrFLZA9QSOijcELs1dvVzs0d4YkCFNcSTYM77fU_-IItE88Y8DkP1kN0RPR6pcJrhFLDfh6cJENxetdmu28gLfmQiB6BrN7B5pc6LNXJUDfapNY5JdOgO0NNb2OphZYX6ZlG_T_fza-uiOoYasku8vrcXjo_sTjHZsVt8JAxJ42Xk0sTR1ck17AKOjwDli17eRYozpJmKT05SjiMx08; TADCID=h_5oYP0_IKwqHNoSABQCmq6heh9ZSU2yA8SXn9Wv5HtdJaPl31iIsOAu8BFGD9mmhlpVZKfAaiJ3MI8kNiJivx3GCDeHSFFkeCY; TART=%1%enc%3AcLxO8gaW0J4DQDzZFpRz3a%2BhPhmQ0boXlcCwAhiB3MMB1LKpzpU%2BGSgUL55X%2BhBB8ZzwB7Grm10%3D; TASSK=enc%3AAJpJV7%2F7f6klBOMnL3N8RA2Zf9Nx0myIGwj8lVbQVSJPNPqTf2M8AKw8DAaZJdEg6NYtXERyjDtIhNLBmozeqbdynnhKUzUpLqVFj1KQgM%2BPc6aWxFmTdodOfkR7zYRE8w%3D%3D; TASameSite=1',
    'dnt': '1',
    'origin': 'https://www.tripadvisor.com.vn',
    'referer': 'https://www.tripadvisor.com.vn/Restaurants-g34047-oa30-Port_Penn_Delaware.html',
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
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}


def crawl(geo_id, city):
    files = []
    data_local_path = f"data_crawl/{city}/restaurants"
    dir_list = os.listdir(data_local_path)
    for file_name in dir_list:
        files.append(file_name)

    offset = 0
    while True:
        payload = get_payload(geo_id, offset)
        try:
            if f"{geo_id}-page{offset}.json" in files:
                print(f"restaurants {geo_id}: {offset} exist")
            else:
                response = requests.request("POST", url, headers=headers, data=payload)
                response = response.json()
                with open(f"data_crawl/{city}/restaurants/{geo_id}-page{offset}.json", "w") as outfile:
                    outfile.write(json.dumps(response))
                print(f"restaurants {geo_id}: crawl offset = {offset} success")
                try:
                    if len(response[0].get("data").get("response").get("restaurants")) < 30:
                        break
                except:
                    break
        except Exception as e:
            log = {
                "payload": payload,
                "offset": offset,
                "error": str(e),
            }

            with open(f"logging/{city}/restaurants/{geo_id}-page{offset}.json", "w") as outfile:
                outfile.write(json.dumps(log))
            print(f"restaurants {geo_id}: crawl offset = {offset} error")
        finally:
            offset += 30

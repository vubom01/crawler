import time

import requests
from bs4 import BeautifulSoup


def get_url(geo_id, city, page):
    return f"https://www.tripadvisor.com.vn/Restaurants-g{geo_id}-oa{page}-{city}.html#LOCATION_LIST"


headers = {
    'Cookie': 'CM=%1%PremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CRestAds%2FRPers%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7Cpv%2C0%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CCrisisSess%2C%2C-1%7CUVOwnersSess%2C%2C-1%7CRestPremRSess%2C%2C-1%7CRepTarMCSess%2C%2C-1%7CCCSess%2C%2C-1%7CCYLSess%2C%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CRestAdsPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7CTSMCPers%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CTADORSess%2C%2C-1%7CAdsRetPers%2C%2C-1%7CListMCSess%2C%2C-1%7CTARSWBPers%2C%2C-1%7CSPMCSess%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7Cmdpers%2C1%2C1707719066%7CRBAPers%2C%2C-1%7CRestAds%2FRSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7CRestPremRPers%2C%2C-1%7CRevHubRMPers%2C%2C-1%7CUVOwnersPers%2C%2C-1%7Csh%2CRuleBasedPopup%2C1707200666%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCrisisPers%2C%2C-1%7CCYLPers%2C%2C-1%7CCCPers%2C%2C-1%7CRepTarMCPers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CTSMCSess%2C%2C-1%7CSPMCPers%2C%2C-1%7CRevHubRMSess%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CAdsRetSess%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CTADORPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CTARSWBSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRestAdsSess%2C%2C-1%7CRBASess%2C%2C-1%7CSPORPers%2C%2C-1%7Cperssticker%2C%2C-1%7CListMCPers%2C%2C-1%7Cmdsess%2C-1%2C-1%7C; ServerPool=C; TAReturnTo=%1%%2FRestaurants-g28929-oa20-Delaware.html; TASession=V2ID.A0C42C1BB987498594010F9BAF171150*SQ.7*LS.Restaurants*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.4743823F4BBA15E7757DBEAD63318E39*FA.1*DF.0*RT.0*TRA.true*LD.28929; TATravelInfo=V2*AY.2024*AM.2*AD.6*DY.2024*DM.2*DD.13*A.2*MG.-1*HP.2*FL.3*DSM.1706864358602*RS.1; TAUD=LA-1707104211277-1*RDD-1-2024_02_02*LG-10055531-2.1.F.*LD-10055532-.....; TAUnique=%1%enc%3AX%2FiE4CdbSizoCEVTOyX2USlBHXRcfYqsp%2Fct9omJ6QyggluDXKQh3wsJvUuiZBwrFZ2%2Bd7y9LSs%3D; datadome=P2DFILhbvx6Y49K99QrdSAs9GmEU0eOffJEw~eTpemWgPVGZTOdUvt_01kHQ3LNbQEnKo6SV83~k_KaY_ryRaxk3KTkNG~NR3_Ngow_VwJ0v3L2Bb~3_qmzHFS0p_plw; PAC=APzy7tYrOXDcyFrmCuCtIivBZDzR_nXzCTrFxGw2u5sFNKDoqfhvQwl9HmAZQmJRsW0Wx6R-TghVIFx8Ru0fDwSFReNfsgcZz_eW3hOEpcAiLxL5tWH5tDAsnNpWS-iceryppk92WXugv2DvEXm7pcLsotbPK7AuguauE8No9ePE; PMC=V2*MS.69*MD.20240118*LD.20240205; SRT=TART_SYNC; TAAUTHEAT=1BGvonqBCq9-6FnMABQCNrrFLZA9QSOijcELs1dvVzs0d4YkCFNcSTYM77fU_-IItE88Y8DkP1kN0RPR6pcJrhFLDfh6cJENxetdmu28gLfmQiB6BrN7B5pc6LNXJUDfapNY5JdOgO0NNb2OphZYX6ZlG_T_fza-uiOoYasku8vrcXjo_sTjHZsVt8JAxJ42Xk0sTR1ck17AKOjwDli17eRYozpJmKT05SjiMx08; TADCID=h_5oYP0_IKwqHNoSABQCmq6heh9ZSU2yA8SXn9Wv5HtdJaPl31iIsOAu8BFGD9mmhlpVZKfAaiJ3MI8kNiJivx3GCDeHSFFkeCY; TART=%1%enc%3AcLxO8gaW0J4DQDzZFpRz3a%2BhPhmQ0boXlcCwAhiB3MMB1LKpzpU%2BGSgUL55X%2BhBB8ZzwB7Grm10%3D; TASID=A0C42C1BB987498594010F9BAF171150; TASSK=enc%3AAJpJV7%2F7f6klBOMnL3N8RA2Zf9Nx0myIGwj8lVbQVSJPNPqTf2M8AKw8DAaZJdEg6NYtXERyjDtIhNLBmozeqbdynnhKUzUpLqVFj1KQgM%2BPc6aWxFmTdodOfkR7zYRE8w%3D%3D; TASameSite=1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}


def get_restaurant_children_ids(geo_id, city):
    print(geo_id, city)
    page = 0
    location_ids = []
    while True:
        ids = []
        for i in range(5):
            print(f"crawl restaurants {get_url(geo_id, city, page)}")
            response = requests.request("GET", get_url(geo_id, city, page), headers=headers)
            soup = BeautifulSoup(response.content, "html.parser")

            if page == 0:
                titles = soup.findAll('div', class_='geo_image')
                links = [link.find('a').attrs["href"] for link in titles]
            if page != 0:
                titles = soup.find('ul', class_='geoList')
                if titles is None:
                    break
                links = [link.attrs["href"] for link in titles.findChildren('a')]

            for link in links:
                data = link.split('-')[1][1:]
                ids.append(data)
            if len(ids) > 0:
                break
            time.sleep(2)
        location_ids += ids
        if len(ids) == 0:
            break
        page += 20
        time.sleep(2)
    return location_ids

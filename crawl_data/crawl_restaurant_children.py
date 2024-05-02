import time

import requests
from bs4 import BeautifulSoup


def get_url(geo_id, city, page):
    return f"https://www.tripadvisor.com.vn/Restaurants-g{geo_id}-oa{page}-{city}.html#LOCATION_LIST"


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Cookie': 'TASameSite=1; TAUnique=%1%enc%3A%2FOacsCHGmtSUsjVVDX5enfsyu%2ByO%2FqyPIbVsNi1qz%2Bd8fL%2BUqsUlcRcNC14G%2FYGrNox8JbUSTxk%3D; TASSK=enc%3AAOfGfXyw65OD9vE%2Bf%2Bj%2FV5qKdrZIiuVH7nCAbHBq3RdCTe40EergFSudo8u%2F%2FO1n1RrLoizcsgUGJd7b2NJmtD5Tcz%2BpKGH46dYkyQhMpRz10tc%2F9PTO1Idko2tJTn3fgQ%3D%3D; VRMCID=%1%V1*id.21047*llp.%2F-a_gclid%5C.Cj0KCQiAyeWrBhDDARIsAGP1mWSzjk916pkAbOFKSgKWbLnlgA__2D__J__5F__p7mZl8ctNHRE6q7mQiXBYQisaQaAl9cEALw__5F__wcB-m21047-a_supac%5C.4188770428-a_supag%5C.13190924659-a_supai%5C.671736848550-a_supbk%5C.1-a_supcm%5C.193220179-a_supdv%5C.c-a_supli%5C.-a_suplp%5C.1028580-a_supnt%5C.g-a_supti%5C.kwd__2D__119671122*e.1703140709392; TATrkConsent=eyJvdXQiOiJBRFYsU09DSUFMX01FRElBIiwiaW4iOiJBTkEsRlVOQ1RJT05BTCJ9; TART=%1%enc%3A1W2gEbMPljElEYLGK6iLfayny1XjtjGI6zlC8rC%2BxgiOxg%2FyLIQ2T2Y8lq%2FKqjcyNox8JbUSTxk%3D; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RS.1; ServerPool=A; PMC=V2*MS.14*MD.20240423*LD.20240424; TADCID=4VMXVOmhnzaD3LhHABQCmq6heh9ZSU2yA8SXn9Wv5H0abMnZpAXhp0BPBCK4I9dyn5UyiPajSTFqb99JgqdlzWdtwBwyyFTlPa0; SRT=TART_SYNC; TASID=AF8F776B41C9460D9DE489E4A7C12B1A; PAC=ANGjurnRhgDuASfmSsiZ0MKC7YDya8xYeiPBxYXmNhYqFJCycUzhOpxMB2Wnnu9YpC48S_iFncwnwWvHzrlByl9mYuj8awfRCfwEGfsZ9QPwPHr2vNuVBo2DxqROLjdUjQ%3D%3D; TAAUTHEAT=GDS7ttlzzcv81ifYABQCNrrFLZA9QSOijcELs1dvVzzxc0tpTkabKWaP4C46sYT2lh1M1IyMNZpLpW6hfDCZERlXwUGuEuq0zxhdvOE79NsgA1IsxSsbYwNqmO7J-tKHGHeRf-ol9Rz7NtJmxPGTR2v9d_Ri3XZXzdI0DQ9HndS51zI90UiUg2adJwpNWEKST5bjANnrZBaRzpBDxS4DzuDpletW2iVDIfXNoekP; TAReturnTo=%1%%2FRestaurants-g294231-Sumatra.html; __gads=ID=de28916d3343f924:T=1700639446:RT=1713940272:S=ALNI_MZXUaS1G9Y-EwGChaE56qnzRhX88Q; __gpi=UID=00000c93f8f8e62b:T=1700639446:RT=1713940272:S=ALNI_MYvmINZPmdXI2KX7Dzv3vE4TeqQuA; __eoi=ID=d924c91a8bc9c535:T=1706759225:RT=1713940272:S=AA-AfjYtsiqdQ9erETJnpVqBTqK7; __vt=nxfNGsEJJxdw57OmABQCwRB1grfcRZKTnW7buAoPsSz4GN2rLtcYRtcMZR4JSvLNu_x6xMSViYtmhk8p56RttjwwVSPmt-F2FARZJB6urXIjSaZ51YPfstTpchjvQlHAwjgnuUDi57WYpch2fxLYBjU5FFE0FzQT3iNpz-6L8vgqsLp3BgV4fSuxnGxnjDe6dALI92IYQtJQEIg; TASession=V2ID.AF8F776B41C9460D9DE489E4A7C12B1A*SQ.50*LS.Restaurants*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.4743823F4BBA15E7757DBEAD63318E39*FA.1*DF.0*RT.0*TRA.true*LD.294231*EAU.4; CM=%1%PremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CRestAds%2FRPers%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7Cpv%2C0%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CCrisisSess%2C%2C-1%7CUVOwnersSess%2C%2C-1%7CRestPremRSess%2C%2C-1%7CRepTarMCSess%2C%2C-1%7CCCSess%2C%2C-1%7CCYLSess%2C%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CRestAdsPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7CTSMCPers%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CTADORSess%2C%2C-1%7CAdsRetPers%2C%2C-1%7CListMCSess%2C%2C-1%7CTARSWBPers%2C%2C-1%7CSPMCSess%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7Cmdpers%2C1%2C1714545380%7CRBAPers%2C%2C-1%7CRestAds%2FRSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7CRestPremRPers%2C%2C-1%7CRevHubRMPers%2C%2C-1%7CUVOwnersPers%2C%2C-1%7Csh%2CRuleBasedPopup%2C1714026980%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCrisisPers%2C%2C-1%7CCYLPers%2C%2C-1%7CCCPers%2C%2C-1%7CRepTarMCPers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CTSMCSess%2C%2C-1%7CSPMCPers%2C%2C-1%7CRevHubRMSess%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CAdsRetSess%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CTADORPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CTARSWBSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRestAdsSess%2C%2C-1%7CRBASess%2C%2C-1%7CSPORPers%2C%2C-1%7Cperssticker%2C%2C-1%7CListMCPers%2C%2C-1%7Cmdsess%2C-1%2C-1%7C; TAUD=LA-1713853357306-1*RDD-2-2024_04_23*ARC-79089124*LG-87223402-2.1.F.*LD-87223403-.....; datadome=JOqTVeDPda0mNTjCL_T~mlZUBG_OQ4~iEUqwUQ0~E0QhaPaerzfSeWPCvfHT~ASx3CdS8Ymbv~3SUZIx5h35GguzGYsNVDtKwegSrq5w4VVPHymv~BS3nAFV6eTdsN1t; roybatty=TNI1625!ANqPRL9OKnoLdeDFkOwNAapLj4yOkkWCbUKvQbsTHDIf9WOdYiGXf188GxAtaEwTG1mmE4FkBYAUgacI1WHtRTlxoCLvfYOTeBsA97uIz9ZNqirwA2ujwrW%2B0dj%2FVi3kz%2B7FnFu3Hnk4darVzv7wRpvZEqHA7fMadKl5mjsBBsptUaJnd2rJF9MW6UHWbfUqrA%3D%3D%2C1'
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

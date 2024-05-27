import time

import requests
from bs4 import BeautifulSoup


def get_url(geo_id, city, page):
    return f"https://www.tripadvisor.com.vn/Restaurants-g{geo_id}-oa{page}-{city}.html#LOCATION_LIST"


headers = {
  'accept': '*/*',
  'accept-language': 'en,vi;q=0.9,en-US;q=0.8',
  'content-type': 'application/json',
  'cookie': 'TASameSite=1; TAUnique=%1%enc%3A93%2FZhYAfzju%2FtVmNgfXL0Yi5FpYuKmsDJApCZtNoVXjZWP4wrupYepX3aEH1CYRTNox8JbUSTxk%3D; TASSK=enc%3AAPF9egxYHR9eR15%2BP2CsMzh8NI2XEG%2Bjf1UI3B%2BtnBqnentjbO7XrBiEyXs9QvDLiRP9vd%2BwuHYyRFT%2BdI3Cr9wfLWYr6eNoEojK9Wdlb1eGTvw2aAkWrguZS7WSgYgt7w%3D%3D; TATrkConsent=eyJvdXQiOiJTT0NJQUxfTUVESUEiLCJpbiI6IkFEVixBTkEsRlVOQ1RJT05BTCJ9; _ga=GA1.1.1797590154.1715134501; pbjs_sharedId=40284df8-ea83-4322-af5d-2221ed3e39c0; pbjs_sharedId_cst=zix7LPQsHA%3D%3D; _li_dcdm_c=.tripadvisor.com.vn; _lc2_fpi=28c87295fd99--01hxazq45t7gpyw35q6mn91afj; _lc2_fpi_meta=%7B%22w%22%3A1715134501051%7D; _lr_env_src_ats=false; pbjs_unifiedID=%7B%22TDID%22%3A%2282725620-db62-42af-b03f-8bb6fafefa4a%22%2C%22TDID_LOOKUP%22%3A%22FALSE%22%2C%22TDID_CREATED_AT%22%3A%222024-05-08T02%3A15%3A11%22%7D; pbjs_unifiedID_cst=zix7LPQsHA%3D%3D; ServerPool=A; TADCID=oZbFpDoErf1T5aPmABQCmq6heh9ZSU2yA8SXn9Wv5H3TQkiT1aVrWT09legf0qCGZWRZ6fn8YDUIFS2lz6uqW1VjL14kTmpY9pk; _lr_sampling_rate=0; pbjs_li_nonid=%7B%7D; pbjs_li_nonid_cst=zix7LPQsHA%3D%3D; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RS.1; TART=%1%enc%3A1W2gEbMPljGMpGpTa8GeK3QPxv%2FaBryAoisSGW1inl0qzYi51DvdKz%2FpC%2B21jkl0Nox8JbUSTxk%3D; PMC=V2*MS.23*MD.20240507*LD.20240527; TAReturnTo=%1%%2FRestaurants-g293959-Pakistan.html; TASID=3405C029654446029BA80AA0AD73F49C; PAC=AFlRszthEXM-K8myA14962wrEcmGGUHKQ71w3ct6xZHY64B9wvyM5KIucZyFXbAJSCnMSwtJmg1attWi7Pltzz93_Lzy9B0QbcyvXuFiWhmzunUKQ8GfMoKQ0O4mnMgifqvTwvritNKzacQd-Ps2oRgtW1yzNDIe8u_HrmweUCin; roybatty=TNI1625!ANAxTXVoCTf3yhBsacsw6UYxAIvykXgw1%2BMMsDcJQJoyxePaz26THMajNH00vvM%2B8ub3OZ48%2Bc7Ar8qc4EMMr6dIRtSMErtDa8OUJ8OZmx%2FO6HKtjx8L2enaOyTQXRWXReGDO5CQ83N8l9h29iSGDaRPU5PiWHENTLHpRCEt7DC8ElRXk251kVu%2B0Ori6A61zQ%3D%3D%2C1; _lr_retry_request=true; __vt=YQpC9nF8XmEHK2QhABQCwRB1grfcRZKTnW7buAoPsS2xuAz7J6hOnNAwl-d0rl5BD0VyRpKT4RipMUq1btOJoOf7DUvty6Hb02wqIg-BmmVHkZNvJkAl_Ef3bNRetk6DwbmJGAwTi-8Q7tyrhcf73ENP; __gads=ID=0e7600e069598041:T=1715134521:RT=1716791747:S=ALNI_MYa0CXNlXE-badceox2XHTG2H9xcQ; __gpi=UID=00000e1249a2cd54:T=1715134521:RT=1716791747:S=ALNI_MbYy0cmxkoEbH7F9W9Ul_x24tf2cw; __eoi=ID=91c723c0aaa5ca94:T=1715134521:RT=1716791747:S=AA-AfjZSyoiu3pA_xp3Tp9ECRLhb; ab.storage.sessionId.6e55efa5-e689-47c3-a55b-e6d7515a6c5d=%7B%22g%22%3A%2245827b32-7c15-8164-387a-c80343b9dc0f%22%2C%22e%22%3A1716791799772%2C%22c%22%3A1716791784773%2C%22l%22%3A1716791784773%7D; ab.storage.deviceId.6e55efa5-e689-47c3-a55b-e6d7515a6c5d=%7B%22g%22%3A%220b91c69b-f633-1a2e-1c5a-c1c3fc637a2c%22%2C%22c%22%3A1715134500764%2C%22l%22%3A1716791784774%7D; _ga_QX0Q50ZC9P=GS1.1.1716790504.5.1.1716791788.18.0.0; TASession=V2ID.3405C029654446029BA80AA0AD73F49C*SQ.138*LS.Restaurants*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*FA.1*DF.0*TRA.true*LD.1203029*EAU._; SRT=TART_SYNC; TAUD=LA-1716779035093-1*RDD-1-2024_05_27*ARC-357700*LG-12755127-2.1.F.*LD-12755128-.....; datadome=EXgHSNS9C8gdc73XuHPgW0kDkkBbT_jfIqoExRHfvcYKRITEfrXSX6EdrnjDxpNG4EBHeakNFWowWYWqHwn~A~KJ8Z9ZAfDj1TKMySM6chlR8FYyoYRTsX6bAu~1CNoD; CM=%1%PremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CRestAds%2FRPers%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7Cpv%2C0%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CCrisisSess%2C%2C-1%7CUVOwnersSess%2C%2C-1%7CRestPremRSess%2C%2C-1%7CRepTarMCSess%2C%2C-1%7CCCSess%2C%2C-1%7CCYLSess%2C%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CRestAdsPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7CTSMCPers%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CTADORSess%2C%2C-1%7CAdsRetPers%2C%2C-1%7CListMCSess%2C%2C-1%7CTARSWBPers%2C%2C-1%7CSPMCSess%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7Cmdpers%2C1%2C1717396665%7CRBAPers%2C%2C-1%7CRestAds%2FRSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7CRestPremRPers%2C%2C-1%7CRevHubRMPers%2C%2C-1%7CUVOwnersPers%2C%2C-1%7Csh%2CRuleBasedPopup%2C1716878265%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCrisisPers%2C%2C-1%7CCYLPers%2C%2C-1%7CCCPers%2C%2C-1%7CRepTarMCPers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CTSMCSess%2C%2C-1%7CSPMCPers%2C%2C-1%7CRevHubRMSess%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CAdsRetSess%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CTADORPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CTARSWBSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRestAdsSess%2C%2C-1%7CRBASess%2C%2C-1%7CSPORPers%2C%2C-1%7Cperssticker%2C%2C-1%7CListMCPers%2C%2C-1%7Cmdsess%2C-1%2C-1%7C; TASession=V2ID.3405C029654446029BA80AA0AD73F49C*SQ.139*LS.Restaurants*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*FA.1*DF.0*RT.0*TRA.true*LD.293959*EAU._; TAUD=LA-1716779035093-1*RDD-1-2024_05_27*ARC-357700*LG-12830661-2.1.F.*LD-12830662-.....; datadome=_6hf~RlUByAnbcSFSu1KAzinvhhkGw0dPrxZx4BxmmHol9xPwHVjV6UBhqFvswJ3x9Dpc0KOvLpZFOYhiKVXa3dn5hAVPIrFDN1moLOOk4cGSPWnT_W4ykeZhnd3IWYQ; TASID=3405C029654446029BA80AA0AD73F49C; TAUnique=%1%enc%3Aa78J7LApo4t77Ro1b2e5YoGxps8aod44oM3pULa26757TkZ3cD5q9RttQuu2CkdqNox8JbUSTxk%3D',
  'origin': 'https://www.tripadvisor.com.vn',
  'priority': 'u=1, i',
  'referer': 'https://www.tripadvisor.com.vn/Restaurants-g1203029-Punjab_Province.html',
  'sec-ch-device-memory': '8',
  'sec-ch-ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
  'sec-ch-ua-arch': '"x86"',
  'sec-ch-ua-full-version-list': '"Chromium";v="124.0.6367.207", "Microsoft Edge";v="124.0.2478.105", "Not-A.Brand";v="99.0.0.0"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-model': '""',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'same-origin',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
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

import time

import requests
from bs4 import BeautifulSoup


def get_url(geo_id, city, page):
    return f"https://www.tripadvisor.com.vn/Restaurants-g{geo_id}-oa{page}-{city}.html#LOCATION_LIST"


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Cookie': 'TASameSite=1; TAUnique=%1%enc%3A%2FOacsCHGmtSUsjVVDX5enfsyu%2ByO%2FqyPIbVsNi1qz%2Bd8fL%2BUqsUlcRcNC14G%2FYGrNox8JbUSTxk%3D; TASSK=enc%3AAOfGfXyw65OD9vE%2Bf%2Bj%2FV5qKdrZIiuVH7nCAbHBq3RdCTe40EergFSudo8u%2F%2FO1n1RrLoizcsgUGJd7b2NJmtD5Tcz%2BpKGH46dYkyQhMpRz10tc%2F9PTO1Idko2tJTn3fgQ%3D%3D; VRMCID=%1%V1*id.21047*llp.%2F-a_gclid%5C.Cj0KCQiAyeWrBhDDARIsAGP1mWSzjk916pkAbOFKSgKWbLnlgA__2D__J__5F__p7mZl8ctNHRE6q7mQiXBYQisaQaAl9cEALw__5F__wcB-m21047-a_supac%5C.4188770428-a_supag%5C.13190924659-a_supai%5C.671736848550-a_supbk%5C.1-a_supcm%5C.193220179-a_supdv%5C.c-a_supli%5C.-a_suplp%5C.1028580-a_supnt%5C.g-a_supti%5C.kwd__2D__119671122*e.1703140709392; TATrkConsent=eyJvdXQiOiJBRFYsU09DSUFMX01FRElBIiwiaW4iOiJBTkEsRlVOQ1RJT05BTCJ9; TADCID=uL3TceSxN1p9BqK1ABQCmq6heh9ZSU2yA8SXn9Wv5H0Uyk7PjKLm_VJ53AO4ZviDt6KSRChk2GwMw2nSv1qOqH4cqfr44QuVsVQ; TAAUTHEAT=TdzDqmHacnCZ21UqABQCNrrFLZA9QSOijcELs1dvVzzryrZbwgroQrMif0a2p2yFQYE-zjdZ5DPz0pbqA0G8XXXzzcNGuU3Bmsi3TVaXkM2lvfkVbp569Qnzh0bjmsPkwSMWYuF8CV1oTxmA9X47PsIEf5Q2Ov0IKnrVsNGbwDdZL6GYgY4kkx14FAEX1goJnRXl7xN8KftZpcdSxE2Q0mZkRTk2uMIA35EB2ZvC; TASID=954B6B551D48A48B51AFB9B3FBE90F6E; PAC=APvFXpnLoa00IUh3wpW00UdfrAfv5_NPygjpFowa0YRBy6ShY83uEPU-P1KkOHtgHdgxdhbhRYTR1rtmZEsnariXWzBjaOx1s_7a5I7enNvjCfJD-9pyfas7yb7QH3UuNg%3D%3D; TART=%1%enc%3A1W2gEbMPljElEYLGK6iLfayny1XjtjGI6zlC8rC%2BxgiOxg%2FyLIQ2T2Y8lq%2FKqjcyNox8JbUSTxk%3D; ServerPool=X; PMC=V2*MS.14*MD.20240423*LD.20240423; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RS.1; __vt=sim-VcVNPWhExoxOABQCwRB1grfcRZKTnW7buAoPsSzypFVcRurDInEaKWctPlzb88VbiFCA55AGVJb3QtgzsDEZjm6hjOo0uJRElt6RFR0m2Dtkack3t5dPbrNrEMxzqGRohMF2kolcXMSPI_P93CGtxsfHWkij2B43ZdMMcSSpIQx0fHtbxdkpYAt--966RDDds4c6vE_G4bI; __gads=ID=de28916d3343f924:T=1700639446:RT=1713856756:S=ALNI_MZXUaS1G9Y-EwGChaE56qnzRhX88Q; __gpi=UID=00000c93f8f8e62b:T=1700639446:RT=1713856756:S=ALNI_MYvmINZPmdXI2KX7Dzv3vE4TeqQuA; __eoi=ID=d924c91a8bc9c535:T=1706759225:RT=1713856756:S=AA-AfjYtsiqdQ9erETJnpVqBTqK7; SRT=TART_SYNC; TAReturnTo=%1%%2FRestaurants-g294231-Sumatra.html; roybatty=TNI1625!ABxDIi6kUq9bFdTmPlkArjQlfxFXXtjrmQBeUeQkxfIr75QcCBy63EQE16ExZ8U9Wl2pnN8zlQO7BKQjgvUDKk13Yow1cCf4gehXiJAoCivLfrmAM%2FRdrLfRKJH7ZVQ2jfV6kBp43xO9yEMv3YJMy5ygUcCjjjbDlgF3PqqDmvSX%2FYnIXLhKBoYYBvPP6AN0KQ%3D%3D%2C1; TASession=V2ID.954B6B551D48A48B51AFB9B3FBE90F6E*SQ.69*LS.DemandLoadAjax*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.4743823F4BBA15E7757DBEAD63318E39*FA.1*DF.0*TRA.true*LD.294231*EAU.4; TAUD=LA-1713853357306-1*RDD-2-2024_04_23*ARC-1249548*LG-3635992-2.1.F.*LD-3635993-.....; datadome=C0776RYLepeUcqerPCECddCqlPmJrZKv2fSdYHVo2YP7hNLiSUvOze~LezWtH4RlapNSDDSrfevR8H5rSvi_Pn0vSzeLyFWrVfCfWtplFZDcN0oZTPlM8mFZI9b0mz6w'
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

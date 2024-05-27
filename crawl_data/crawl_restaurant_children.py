import time

import requests
from bs4 import BeautifulSoup


def get_url(geo_id, city, page):
    return f"https://www.tripadvisor.com.vn/Restaurants-g{geo_id}-oa{page}-{city}.html#LOCATION_LIST"


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Cookie': 'TADCID=IWihbvaUo-zqeZa9ABQCmq6heh9ZSU2yA8SXn9Wv5H3TZ4CbIGpaQwIIIt6e6ET0vfFhaVzeT7dJdeXBk2RGwM82fl9qRN6wkyo; TASameSite=1; TAUnique=%1%enc%3AqlTlfK5z7%2BwqO5x4NZhJfqZQmoCr2I4bE2RXU5p%2FaoNCGimyycx4r7TfrrmmvwABNox8JbUSTxk%3D; __vt=sEKLfVxzk9emLrQ5ABQCwRB1grfcRZKTnW7buAoPsS2xB6qF2Sv075JNENNFC4QBXA2FNBHA7Sv_FDhNrnaextmSkffXUgpvuZ7Vo01TPoSoLECnDnZxh7TV8lVlxNkS7Oe0Ezxc122e9eH6P6xA3_Yt4A; TASID=606D864E26CA5FAF293252DF3DF40864; TASSK=enc%3AAHxr1NpvFob5g2mS2beqZsVqzpApGR84NxDScTC2C85Up2QJahK07Tu8sSVku3T2iYg5b4odc6%2Ff%2BZdsY%2FkXGTrB2dXaf0tyooNInW379LwK%2BYSZzTPN%2BpBPgTnAORVJJQ%3D%3D; TART=%1%enc%3A1W2gEbMPljFEu%2FTBq1UGSmdKf8jCIaL8gZlcpxZoLsjayjLhHpk7qPnclctxVDTINox8JbUSTxk%3D; TATrkConsent=eyJvdXQiOiJTT0NJQUxfTUVESUEiLCJpbiI6IkFEVixBTkEsRlVOQ1RJT05BTCJ9; pbjs_sharedId=08ffa8f0-395f-426d-be6d-f2b770401a19; pbjs_sharedId_cst=zix7LPQsHA%3D%3D; _li_dcdm_c=.tripadvisor.com.vn; _lc2_fpi=28c87295fd99--01hyw21832w2755v997rk8cmp7; _lc2_fpi_meta=%7B%22w%22%3A1716781097058%7D; _ga=GA1.1.1510043401.1716781097; __gads=ID=abd3b64c4e44dd42:T=1716781100:RT=1716781100:S=ALNI_MZ9lQNTTBqeKRSEIdq7FOvxL8pwpw; __gpi=UID=00000e2e7930feda:T=1716781100:RT=1716781100:S=ALNI_Mb-JTsfTFS8P79gXDtWC_x2K3d79A; __eoi=ID=c7f334398915eab6:T=1716781100:RT=1716781100:S=AA-AfjaO-NtfDVjBp6tMIR_RLeXU; _lr_sampling_rate=100; _lr_retry_request=true; _lr_env_src_ats=false; pbjs_unifiedID=%7B%22TDID%22%3A%221c7b7674-9d7d-4814-b479-ac92bc5d7c92%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222024-04-27T03%3A38%3A27%22%7D; pbjs_unifiedID_cst=zix7LPQsHA%3D%3D; pbjs_li_nonid=%7B%7D; pbjs_li_nonid_cst=zix7LPQsHA%3D%3D; PAC=AJs2weEXWrbXctCZKeHFBfYtFJ4hWsM-nCP7D3jkl-2gF_9rIKTx8qefUiG2iPFKx7KqyarhiSvy63VDXSlB2W0eNgkDjdxVQbTgRH8NlgSoutShHR22EdQypz95nAggbQ%3D%3D; SRT=TART_SYNC; ServerPool=X; PMC=V2*MS.44*MD.20240526*LD.20240526; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RS.1; TAUD=LA-1716781156224-1*RDD-1-2024_05_26*LG-328-2.1.F.*LD-329-.....; datadome=hd1ax7y3s0eDsTCSuRe649JJ48mBD~yY3V39~np6tnDnUw8P6ZAvrSFW86tOJLKWC7SVRnMwa4Do7IiZ4Bm2WcYt7nK1hILzoCiUGTHkNMa~sGxjgod3MJU7r5Ao1cje; TASession=V2ID.606D864E26CA5FAF293252DF3DF40864*SQ.4*LS.Search*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*FA.1*DF.0*TRA.true*EAU._; _ga_QX0Q50ZC9P=GS1.1.1716781097.1.1.1716781157.60.0.0; ab.storage.deviceId.6e55efa5-e689-47c3-a55b-e6d7515a6c5d=%7B%22g%22%3A%222a80fc3b-0d52-2fb2-ebf6-51984ca8ab54%22%2C%22c%22%3A1716781097360%2C%22l%22%3A1716781157779%7D; ab.storage.sessionId.6e55efa5-e689-47c3-a55b-e6d7515a6c5d=%7B%22g%22%3A%222954cafc-39d8-8670-9852-c77c9f4e807d%22%2C%22e%22%3A1716781175740%2C%22c%22%3A1716781157778%2C%22l%22%3A1716781160740%7D'
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
            print(soup)
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

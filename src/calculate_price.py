import time

import requests
from src.choose_item import choose_item
import math

# headers = {
#     "User-Agent": "Mozilla/5.0"
# }

def cena(title, category_id, current_price, headers):
    try:
        oglasi = iscitaj_sve_oglase(title, category_id, headers)
        if not oglasi:
            return current_price
        cijena, id_prodavca = najniza_cijena(title, oglasi, category_id)
        if not id_prodavca:
            return current_price
        cijena = odredi_nasu_novu_cijenu(cijena, id_prodavca)
        return cijena
    except:
        print("Greska pri racunanju cijene")
        return current_price

# def iscitaj_sve_oglase(title, category_id, headers):
#     try:
#         naziv = title.replace(" ", "+")
#
#         if category_id == 1499:
#             category_id = ""
#
#         oglasi = "https://olx.ba/api/search?&attr=&attr_encoded=1&q=" + naziv + "&sort_by=price&sort_order=asc&category_id=" + str(category_id) + "&state=1&page=1&per_page=100"
#
#         response = requests.get(oglasi, headers=headers)
#
#         if response.status_code != 200:
#             time.sleep(3)
#             iscitaj_sve_oglase(title, category_id, headers)
#
#         data = response.json()
#         oglasi = [(oglas["title"], oglas["discounted_price_float"], oglas["user_id"]) for oglas in data["data"]]
#         return oglasi
#     except:
#         time.sleep(2)

def iscitaj_sve_oglase(title, category_id, headers):
    try:
        naziv = title.replace(" ", "+")

        if category_id == 1499:
            category_id = ""

        base_url = "https://olx.ba/api/search"

        params_common = {
            "attr": "",
            "attr_encoded": 1,
            "q": naziv,
            "category_id": category_id,
            "state": 1,
            "page": 1,
            "per_page": 100
        }

        # 🔼 Rastuće cijene
        params_asc = params_common.copy()
        params_asc.update({
            "sort_by": "price",
            "sort_order": "asc"
        })

        response_asc = requests.get(base_url, headers=headers, params=params_asc)
        response_asc.raise_for_status()

        data_asc = response_asc.json()
        oglasi_asc = [
            (oglas["title"], oglas.get("discounted_price_float"), oglas["user_id"])
            for oglas in data_asc["data"]
        ]

        # 🔽 Opadajuće cijene
        params_desc = params_common.copy()
        params_desc.update({
            "sort_by": "price",
            "sort_order": "desc"
        })

        response_desc = requests.get(base_url, headers=headers, params=params_desc)
        response_desc.raise_for_status()

        data_desc = response_desc.json()
        oglasi_desc = [
            (oglas["title"], oglas.get("discounted_price_float"), oglas["user_id"])
            for oglas in data_desc["data"]
        ]

        return {
            "rastuce": oglasi_asc,
            "opadajuce": oglasi_desc
        }

    except requests.RequestException as e:
        print("Greška:", e)
        time.sleep(2)
        return None



def najniza_cijena(prilagodjen_naziv, oglasi, category_id):
    # Prvo pretrazujemo tudje profile, a ako ne postoji onda pretrazujemo svoje
    for oglas in oglasi["rastuce"]:
        naziv_oglasa, cijena, id_prodavca = oglas
        if (choose_item(category_id, prilagodjen_naziv, naziv_oglasa)) and (id_prodavca in subotica.values()):
            # print(naziv_oglasa)
            return cijena, id_prodavca
    for oglas in oglasi["opadajuce"]:
        naziv_oglasa, cijena, id_prodavca = oglas
        if (choose_item(category_id, prilagodjen_naziv, naziv_oglasa)) and (id_prodavca in nasi_profili.values()):
            # print(naziv_oglasa)
            return cijena, id_prodavca

    return False, False

def odredi_nasu_novu_cijenu(najniza_cijena, id_prodavca):
    if id_prodavca in nasi_profili.values():
        return math.ceil(najniza_cijena)
    else:
        return math.ceil(najniza_cijena - 1)

nasi_profili = {
    "TechZone": 261905,
    "DrPC": 1588921,
    "Teslashop": 1011681,
    "StoreComputer": 1333165,
    "BetaTech": 3128221,
    "MaxyShop": 3158396,
    "TargetTech": 3109742,
    "CompElite": 3452303,
    "CompX" : 3527815,
    "DigitalForge" : 798981,    # Vladan
    "AMTechShop" : 1151645,     # Avram
    "KomponenteEU": 4082244,
}

tudji_profili = {
    "TehnoLix": 347657,
    "MegaTechno": 290226,
    "PcLux": 123679,
    "GamingShopBN": 3403766,
    "SrkiTech": 41785,
    "TechyBubble": 12728,
    "LuxTehnika": 328356,
    "SvetTehnike": 59418,
    "ComputerCentar": 30107,
    "InsertHome": 534901,
    "mickey84": 70212,
    "PCBest": 81513,
    "PC_ONER": 1599378,
    "MoGame": 1024366,
    "CPU_Infotech": 802229,
    "SLOTracunari": 14499,
    "Didakta": 6629,
    "ctech": 1886406,
    "PcOner": 2625257,
    "DigitalTech": 39288,
    "B2M": 3579069,
    "Home_Tech": 213752,
    "ETechShop": 149934,
    "GeekZona": 290226,
    "DejoproTech123": 3756215
}

subotica = {
    "SrkiTech": 41785,              # Subotica
    "TechyBubble": 12728,           # Subotica
    "LuxTehnika": 328356,           # Subotica
    "SvetTehnike": 59418,           # Subotica
    "DigitalTech": 39288,           # Subotica
    "GeekZona": 290226,             # Subotica
    "ELEKTRO_VUCKO" : 64096278,     # Subotica
}

svi_profili = nasi_profili | tudji_profili

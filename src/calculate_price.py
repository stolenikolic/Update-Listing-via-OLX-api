import time

import requests
from src.choose_item import choose_item
import math

# headers = {
#     "User-Agent": "Mozilla/5.0"
# }

def cena(title, category_id, headers):
    try:
        oglasi = iscitaj_sve_oglase(title, category_id, headers)
        if not oglasi:
            print("Po dogovoru")
            return 0
        cijena, id_prodavca = najniza_cijena(title, oglasi, category_id)
        cijena = odredi_nasu_novu_cijenu(cijena, id_prodavca)
        return cijena
    except:
        print("Greska pri racunanju cijene")
        return 0

def iscitaj_sve_oglase(title, category_id, headers):
    try:
        naziv = title.replace(" ", "+")

        if category_id == 1499:
            category_id = ""

        oglasi = "https://olx.ba/api/search?&attr=&attr_encoded=1&q=" + naziv + "&sort_by=price&sort_order=asc&category_id=" + str(category_id) + "&state=1&page=1&per_page=100"

        response = requests.get(oglasi, headers=headers)

        if response.status_code != 200:
            time.sleep(3)
            iscitaj_sve_oglase(title, category_id, headers)

        data = response.json()
        oglasi = [(oglas["title"], oglas["discounted_price_float"], oglas["user_id"]) for oglas in data["data"]]
        return oglasi
    except:
        time.sleep(2)



def najniza_cijena(prilagodjen_naziv, oglasi, category_id):
    # Prvo pretrazujemo tudje profile, a ako ne postoji onda pretrazujemo svoje
    for oglas in oglasi:
        naziv_oglasa, cijena, id_prodavca = oglas
        if (choose_item(category_id, prilagodjen_naziv, naziv_oglasa)) and (id_prodavca in tudji_profili.values()):
            # print(naziv_oglasa)
            return cijena, id_prodavca
    for oglas in oglasi:
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
    "maksa001": 3452303,
    "Dado" : 3527815,
    "DigitalForge" : 798981,    # Vladan
    "AMTechShop" : 1151645,     # Avram
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

svi_profili = nasi_profili | tudji_profili

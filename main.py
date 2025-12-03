import requests
import headers
from src import products
import unos_podataka

profile = "Dado"
headers_IPON = headers.headers_IPON
headers_OLX = headers.get_headers_OLX(profile)
response = None

products.all_products("https://olx.ba/api/users/" + "RaleTechnology" + "/listings?sort_by=date&sort_order=asc&per_page=200&category_id=0&page=", headers_IPON, 1)
allProducts = products.read_products()
start_index = products.get_start_index()

for i, product in enumerate(allProducts[start_index:], start=start_index):
    try:
        id_artikla = str(allProducts[i]["id_artikla"])

        data = {
            "description": unos_podataka.ubaci_opis(profile),
        }

        response = requests.put(f"https://api.olx.ba/listings/{str(id_artikla)}", headers=headers_OLX, json=data)
        publish = requests.post(f"https://api.olx.ba/listings/{str(id_artikla)}/publish", headers=headers_OLX)

        print(i, ": NOVO")
        products.save_last_index(i)
    except:
        if response:
            products.check_daily_limit(response)

products.delete_data()
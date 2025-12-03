import requests
from src import headers
from src import products
from src.calculate_price import cena
from src.search_title import optimize_title_for_search

profile = "DrPC"
headers_IPON = headers.headers_IPON
headers_OLX = headers.get_headers_OLX(profile)
response = None

products.all_products("https://olx.ba/api/users/" + "DrPC" + "/listings?sort_by=date&sort_order=asc&per_page=200&category_id=0&page=", headers_IPON, 1)
allProducts = products.read_products()
start_index = products.get_start_index()

while start_index < len(allProducts):
    try:
        id_artikla = str(allProducts[start_index]["id_artikla"])
        title = allProducts[start_index]["title"]
        category_id = allProducts[start_index]["category_id"]
        optimized_title_for_search = optimize_title_for_search(title, category_id)
        calculated_price_km = cena(optimized_title_for_search, category_id, headers_OLX)

        data = {
            "price": calculated_price_km,
        }

        response = requests.put(f"https://api.olx.ba/listings/{str(id_artikla)}", headers=headers_OLX, json=data)
        publish = requests.post(f"https://api.olx.ba/listings/{str(id_artikla)}/publish", headers=headers_OLX)

        print(f"{start_index}/{len(allProducts)}", title)
        start_index += 1
        products.save_last_index(start_index)
    except:
        if response:
            products.check_daily_limit(response)

products.delete_data()
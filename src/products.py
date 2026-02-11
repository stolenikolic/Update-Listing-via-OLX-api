import requests
import json
# import headers
import os


def all_products(API_LINK, headers, start_page=1, all_products=[]):
    while True:
        if os.path.exists("products.json"):
            break

        url = API_LINK + str(start_page)
        if len(all_products) <= 9999:
            response = requests.get(url, headers=headers)
            data = response.json()
            items = data.get("data", [])
        else:
            with open("products.json", "w", encoding="utf-8") as f:
                json.dump(all_products, f, ensure_ascii=False, indent=2)
            break

        if len(data['data']) == 0:
            with open("products.json", "w", encoding="utf-8") as f:
                json.dump(all_products, f, ensure_ascii=False, indent=2)
            break

        for item in items:
            product = {
                "id_artikla": item.get("id"),
                "title" : item.get("title"),
                "category_id": item.get("category_id"),
                "current_price": item.get("discounted_price_float"),
            }
            all_products.append(product)
        start_page += 1

    # return all_products


def read_products():
    with open("products.json", "r", encoding="utf-8") as f:
        allProducts = json.load(f)
    return allProducts


def get_start_index():
    if os.path.exists("progress.json"):
        with open("progress.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            start_index = data.get("last_index")
    else:
        start_index = 0

    return start_index


def save_last_index(i):
    with open("progress.json", "w", encoding="utf-8") as f:
        json.dump({"last_index": i + 1}, f)


def delete_data():
    print("Brisem podatke")
    os.remove('products.json')
    os.remove('progress.json')


def check_daily_limit(response):
    text = json.loads(response.text)
    print(text["error"]["message"])
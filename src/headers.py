import requests

def get_headers_OLX(profile):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {tokeni_OLX[profile]}",
        "User-Agent": "Mozilla/5.0"
    }
    return headers

def get_ipon_cookie():
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    session.get("https://iponcomp.com/", headers=headers, timeout=10)
    cookie_string = "; ".join([f"{k}={v}" for k, v in session.cookies.get_dict().items()])
    return cookie_string

tokeni_OLX = {
    "TechZone" : "32377613|SKFENIY3npMkW8n9r0HEmmSRUJuUbTOO96LbaXyB",
    "Dado" : "32333933|yeTtVoz2jyHaSP652IzOoriFUxkDxdNXhLQaH05G",
    "Maksa" : "32334082|AIfl74S8OGqsirgNKFuZr8THQd3S55KTNcW29Vml",
    "Avram" : "32854058|6wYV0sJKMf6IBMzd5LHPFs9rfkAPBiFlNfaz77Bh",
    "Vladan" : "32854127|28Fg97D1qfaXECi6qoDWB98lsLHstySWTHVwXywA",
    "Zoran" : "32854182|nQdjpesEHtlob3dm8peWojl1MxwUwDNC6DiBGiS0",
    "DrPC" : "32335050|n85KqpvwLosxNEfAFnXOAddRSpCJHxLbV6rY7zpF",
    }

headers_IPON = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://iponcomp.com/shop/",
    "X-Requested-With": "XMLHttpRequest",
    "x-csrf-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJjc3JmIiwibmJmIjoxNzU2NTYwMzMyLjIzMzU4NCwiZXhwIjoxNzU2NjQ2NzMyLjIzMzYyLCJpc3MiOiJodHRwczovL2lwb25jb21wLmNvbSIsImF1ZCI6Imh0dHBzOi8vaXBvbmNvbXAuY29tIiwianRpIjoiYjFhNzgxYzctYzc3Zi00ODUzLThkZjctZTMyN2YzYzM5YzdhIiwiaWF0IjoxNzU2NTYwMzMyLjIzMzY3NX0.rcoxRzeZs0F5ADsm_ZMUzlDkH-MGa3roq8-Td0v_3gk",
    "Cookie": f"x-ddos-uniq=foobar; {get_ipon_cookie()}"
}
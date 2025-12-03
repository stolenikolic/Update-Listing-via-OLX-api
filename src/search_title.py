import re
from os import remove


def optimize_title_for_search(title, category_id):
    categories = {
        "mouse" : 162,
        "CPU": 167,
        "internal_ssd" : 155,
        "memory": 161,
        "headset": 1499,
        "keyboard": 170,
        "mouse_keyboard_set": 1521,
        "speaker": 1496,
    }

    if categories["mouse"] == category_id:
        title = search_mouse(title)
    elif categories["CPU"] == category_id:
        title = search_cpu(title)
    elif categories["internal_ssd"] == category_id:
        title = search_ssd(title)
    elif categories["memory"] == category_id:
        title = search_ram(title)
    elif categories["headset"] == category_id:
        title = search_headset(title)
    elif categories["keyboard"] == category_id:
        title = search_keyboard(title)
    elif categories["mouse_keyboard_set"] == category_id:
        title = search_mkset(title)
    elif categories["speaker"] == category_id:
        title = search_speaker(title)

    return title

def letter_number_combination_chech(word):
    letter = any(c.isalpha() for c in word)
    number = any(c.isdigit() for c in word)
    return letter and number

def search_cpu(item_name):
    words = item_name.split()
    optimized_title = []

    for word in words:
        if "GHz" in word or "GHZ" in word.upper():
            break
        optimized_title.append(word)

    optimized_title =  " ".join(optimized_title)

    if "BOX" in item_name:
        optimized_title += " BOX"

    return optimized_title

def search_ram(item_name):
    if "KIT" in item_name:
        item_name = item_name.split("KIT")[0] + "KIT"
    elif "CL" in item_name:
        cl_index = item_name.find("CL")
        if cl_index != -1:
            item_name = item_name[:cl_index+4]

    return item_name

def search_ssd(item_name):
    item_name = item_name.upper()
    if "M.2" in item_name:
        parts = item_name.split("M.2")
        item_name = parts[0] + "M.2"
    if "SATA" in item_name:
        parts = item_name.split("SATA")
        item_name = parts[0] + "SATA"

    return item_name

def search_mbo(item_name):
    if "rev." in item_name:
        delovi = item_name.split()
        item_name = " ".join(delovi[:-2])
    return item_name

def title_CASE(naziv_artikla):
    naziv_artikla = naziv_artikla.upper()
    naziv_artikla = naziv_artikla.replace("-", "")
    naziv_artikla = naziv_artikla.replace("ARGB", "")
    naziv_artikla = naziv_artikla.replace("CONTROLLER", "")
    naziv_artikla = naziv_artikla.replace("BRIGHT", "")
    naziv_artikla = naziv_artikla.replace("STOP", "")
    naziv_artikla = naziv_artikla.replace("SHOP", "")
    naziv_artikla = naziv_artikla.replace("GLASS", "")
    naziv_artikla = naziv_artikla.replace("WITH", "")
    naziv_artikla = naziv_artikla.replace("CLEAR", "")
    naziv_artikla = naziv_artikla.replace("WINDOW", "")
    boje = ["BLACK", "WHITE", "BLUE", "RED", "GREEN", "GRAY", "ORANGE", "PINK", "PURPLE", "GREY", "BROWN",
            "YELLOW"]  # Lista imena boja koje želite izbaciti

    for boja in boje:
        naziv_artikla = naziv_artikla.replace(boja, "")

    naziv_artikla = re.sub(r"\s+", " ", naziv_artikla)  # Izbacivanje vise od jednog razmaka
    return naziv_artikla

def title_MOUSE(naziv_artikla):
    naziv_artikla = naziv_artikla.upper()
    boje = ["BLACK", "WHITE", "BLUE", "RED", "GREEN", "GRAY", "ORANGE", "PINK", "PURPLE", "GREY", "BROWN", "YELLOW"]
    naziv_artikla = naziv_artikla.replace("-", " ")
    naziv_artikla = naziv_artikla.replace("/", " ")

    for boja in boje:
        naziv_artikla = naziv_artikla.replace(boja, "")

    naziv_artikla = re.sub(r"\s+", " ", naziv_artikla)  # Izbacivanje vise od jednog razmaka
    print(naziv_artikla)
    return naziv_artikla

def title_HDD(naziv_artikla):
    if "SATA" in naziv_artikla:
        return naziv_artikla.split("SATA")[0].strip()
    return naziv_artikla

def title_MONITOR(naziv_artikla):
    sve_rijeci = naziv_artikla.split()
    brend = sve_rijeci[0]

    rijeci = re.findall(r'\b\w+\b', naziv_artikla)
    kombinacije = []

    for rijec in rijeci:
        if any(char.isdigit() for char in rijec) and any(char.isalpha() for char in rijec):
            kombinacije.append(rijec)

    naziv_artikla = brend + " " + " ".join(kombinacije)
    print(naziv_artikla)
    return naziv_artikla

def search_case(title):
    words = title.split()
    if words[0] == "MS" and words[1] == "INDUSTRIAL":
        words.remove(words[1])
        title = " ".join(words)
    return title


def search_mouse(title):
    if ("HP" in title or "LOGITECH" in title) and "WIRELESS" in title:
        index = title.find("WIRELESS")
        title = title[:index].strip()

    title = title.upper()

    if "GAMING MOUSE" in title:
        title = title.replace("GAMING MOUSE", "")
    if "MOUSE" in title:
        title = title.replace("MOUSE", "")

    if "LOGITECH" in title:
        if "BLUETOOTH" in title:
            title = title.replace("BLUETOOTH", "")
        if "WIRELESS" in title:
            index = title.find("WIRELESS")
            title = title[:index + len("wireless")].strip()
        if "WIRED" in title:
            index = title.find("WIRED")
            title = title[:index].strip()

    if "  " in title:
        title = title.replace("  ", "")

    # print(title)
    return title

def search_headset(title):
    if "LOGITECH" in title:
        if "G733" in title or "G435" in title:
            title = " ".join(title.split()[:3])

    if "aktív zajkioltással" in title:
        title = title.replace("aktív zajkioltással", "active noise cancellation")

    return title

def search_keyboard(title):
    title = title[:55]

    return title

def search_mkset(title):
    title = title[:55]
    title_words = title.split()

    filter = ["LOGITECH", "DELL", "REDRAGON", "ASUS", "GIGABYTE", "MSI"]
    if "MSI" in title and letter_number_combination_chech(title_words[3]):
        title = " ".join(title.split()[:4])
    elif "LOGITECH" in title and letter_number_combination_chech(title_words[2]):
        title = " ".join(title.split()[:3])
    elif title_words[0] in filter and letter_number_combination_chech(title_words[1]):
        title = " ".join(title.split()[:2])

    return title

def search_speaker(title):
    title_words = title.split()

    if letter_number_combination_chech(title_words[1]):
        if "GENIUS" == title_words[0]:
            title = " ".join(title_words[:3])
        else:
            title = " ".join(title_words[:2])

    if "Soundbar" in title_words:
        index = title_words.index("Soundbar")
        title = " ".join(title_words[:index])


    return title

# print(search_speaker("HISENSE HS2000 2.1 DTS/DD Soundbar black"))
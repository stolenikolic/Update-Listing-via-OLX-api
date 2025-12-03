import re

def choose_item(category_id, naziv_artikla, naziv_oglasa):
    categories = {
        "motherboard": 160,
        "water_cooling" : 152,
        "power_supply": 1042,
        "mouse": 162,
        "CPU": 167,
        "internal_ssd": 155,
        "memory": 161,
        "headset": 1499,
        "keyboard": 170,
        "mouse_keyboard_set": 1521,
        "speaker": 1496,
    }
    if category_id == categories['motherboard']:
        return choose_mbo(naziv_artikla, naziv_oglasa)
    elif category_id == categories['mouse']:
        return choose_mouse(naziv_artikla, naziv_oglasa)
    elif category_id == categories['internal_ssd']:
        return choose_ssd(naziv_artikla, naziv_oglasa)
    elif category_id == categories['water_cooling']:
        return choose_water_cooler(naziv_artikla, naziv_oglasa)
    elif category_id == categories['power_supply']:
        return choose_psu(naziv_artikla, naziv_oglasa)
    elif category_id == categories['headset']:
        return choose_headset(naziv_artikla, naziv_oglasa)
    else:
        return True

def choose_ram(naziv_artikla, naziv_oglasa):
    naziv_oglasa = naziv_oglasa.upper()
    naziv_artikla = naziv_artikla.upper()

    if "KIT" in naziv_artikla:
        naziv_artikla = naziv_artikla.split("KIT")[0] + "KIT"
    elif "CL" in naziv_artikla:
        cl_index = naziv_artikla.find("CL")
        if cl_index != -1:
            naziv_artikla = naziv_artikla[:cl_index + 4]

    if "KIT" in naziv_oglasa:
        naziv_oglasa = naziv_oglasa.split("KIT")[0] + "KIT"
    elif "CL" in naziv_oglasa:
        cl_index = naziv_oglasa.find("CL")
        if cl_index != -1:
            naziv_oglasa = naziv_oglasa[:cl_index + 4]

    skup_reci1 = naziv_artikla.split()  # Razdeli prvi string na reči
    skup_reci2 = naziv_oglasa.split()

    if skup_reci1 == skup_reci2:
        # print("Naziv oglasa je: " + naziv_oglasa)
        return True  # Sve reči se poklapaju
    else:
        return False  # Postoje različite reči

def choose_mouse(naziv_artikla, naziv_oglasa):
    naziv_artikla = naziv_artikla.upper()
    naziv_oglasa = naziv_oglasa.upper()

    filter1 = ["I", "II", "III"]
    for f in filter1:
        if f in naziv_artikla and f not in naziv_oglasa:
            return False

    filter2 = ["D-", "O-", "PRO", "MATT", "CORE", "AIMPOINT", "MINI"]
    for f in filter2:
        if (f in naziv_artikla and f not in naziv_oglasa) or (f in naziv_oglasa and f not in naziv_artikla):
            return False

    if ("STEELSERIES" in naziv_artikla or "HP" in naziv_artikla or "XTRFY" in naziv_artikla) and ("WIRELESS" in naziv_oglasa and "WIRELESS" not in naziv_artikla):
        return False

    return True

def choose_ssd(naziv_artikla, naziv_oglasa):
    naziv_oglasa = naziv_oglasa.upper()
    naziv_artikla = naziv_artikla.upper()
    rijeci_artikla = naziv_artikla.split()
    for rec in rijeci_artikla:
        if rec not in naziv_oglasa:
            return False
            break
    else:
        return True


def choose_mbo(naziv_artikla, naziv_oglasa):
    naziv_artikla = naziv_artikla.upper()
    naziv_oglasa = naziv_oglasa.upper()

    if 'D4' in naziv_oglasa:
        if not 'D4' in naziv_artikla:
            return False
    elif 'DDR4' in naziv_oglasa:
        if not 'DDR4' in naziv_artikla:
            return False

    skup_rijeci = naziv_artikla.split()
    for rijec in skup_rijeci:
        if not rijec in naziv_oglasa:
            return False
    return True


def choose_psu(naziv_artikla, naziv_oglasa):
    if ("BE QUIET!" in naziv_artikla)  and ("M" in naziv_oglasa and "M" not in naziv_artikla):
        return False

    return True

def choose_headset(naziv_artikla, naziv_oglasa):
    filter1 = ["I", "II", "III"]
    for f in filter1:
        if f in naziv_artikla and f not in naziv_oglasa:
            return False

    return True

def choose_water_cooler(naziv_artikla, naziv_oglasa):
    if ("DEEPCOOL" in naziv_artikla) and (("SE" in naziv_oglasa and "SE" not in naziv_artikla) or ("Marrs" in naziv_oglasa and "Marrs" not in naziv_artikla)):
        return False

    if ("ENERMAX" in naziv_artikla) and ("SR" in naziv_oglasa and "SR" not in naziv_artikla):
        return False

    return True

# print(choose_water_cooler("DEEPCOOL LE500", "DEEPCOOL LE500"))
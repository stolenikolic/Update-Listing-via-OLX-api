def ubaci_opis(profile):
    profile += ".txt"
    with open("./Opisi/" + profile, "r", encoding="utf-8") as f:
        opis = f.read()
    opis = opis.replace("\n", "<br>")
    return opis
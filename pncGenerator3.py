import json
import time
import re
import subprocess


def process_curl_command(curl_command):
    result = subprocess.run(curl_command, capture_output=True, text=True)
    output = result.stdout

    match = re.search(r'get_document.php\?([^"}]+)', output)

    if match:
        ts_code = match.group(1)
        print("ts_code:", ts_code)

        new_curl_command = [
            'curl',
            '-X', 'POST',
            '-H', 'Accept: application/json',
            '-H', 'Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjExMjUifQ.tsM84PLvbXsvSoNJDTRrSWrfsUKusdRw1jah72v9H08',
            f'10.20.1.4/api/get_document.php?ts_code={ts_code}'
        ]

        new_result = subprocess.run(
            new_curl_command, capture_output=True, text=True)
        new_output = new_result.stdout

        print(new_output)

        file_doc_match = re.search(r'\\/pdfs\\/(.+)"', new_output)
        if file_doc_match:
            file_doc = file_doc_match.group(1)
            print("file_doc:", file_doc)

            url = "http://10.20.1.4/pdfs/{}".format(file_doc)
            wget_command = ['wget', url]
            subprocess.run(wget_command)

        else:
            print("No file_doc found")

    else:
        print("No ts_code found")


def parcourir_fichier_json(nom_fichier):
    # Ouverture du fichier JSON avec l'encodage UTF-8
    with open(nom_fichier, 'r', encoding='utf-8') as fichier:
        # Chargement du contenu JSON dans un dictionnaire
        data = json.load(fichier)

        # Retourne le dictionnaire
        return data


# Exemple d'utilisation
nom_fichier = "excel_document.json"
dictionnaire = parcourir_fichier_json(nom_fichier)
# print(dictionnaire)

for item in dictionnaire:
    taxe_name = item['taxe_name']
    amount = item['amount']
    date = item['date']
    direction = item['direction']
    num_document = item['num_document']
    nom_document = item['nom_document']
    date_edition = item['date_edition']
    ann_validite = item['ann_validite']
    tel_1 = item['tel_1']
    address = item['address']
    company = item['company']
    niu = item['niu']
    rccm = item['rccm']
    type_company = item['type_company']
    type_activity = item['type_activity']
    brand = item['brand']
    model = item['model']
    num_chassis = item['num_chassis']
    color = item['color']
    registration = item['registration']
    model_year = item['model_year']
    fuel_type = item['fuel_type']

    place_of_birth = item['place_of_birth']
    nationality = item['nationality']
    date_of_birth = item['date_of_birth']
    driving_licence_category = item['driving_licence_category']
    child = item['child']
    parental_authority = item['parental_authority']
    msisdn_credit = item['msisdn_credit']
    msisdn_debit = item['msisdn_debit']
    transid = item['transid']

    date_renouvelement = item['date_renouvelement']
    date_expiration = item['date_expiration']
    nom = item['nom']
    prenom = item['prenom']
    seller = item['seller']
    buyer = item['buyer']

    tel_2 = item['tel_2']
    mail = item['mail']
    seller_tel = item['seller_tel']
    buyer_tel = item['buyer_tel']
    seller_address = item['seller_address']
    buyer_address = item['buyer_address']
    parental_authority = item['parental_authority']
    sexe = item['sexe']
    licence_number = item['licence_number']
    carte_grise = item['carte_grise']
    old_carte_grise = item['old_carte_grise']

    old_carte_grise = item['old_carte_grise']
    genre = item['genre']
    Type = item['type']
    engine = item['engine']
    transmission = item['transmission']
    old_color = item['old_color']
    curb_weight = item['curb_weight']
    gross_weight = item['gross_weight']
    power = item['power']
    drivetrain = item['drivetrain']

    json_data = {"msisdn_credit": msisdn_credit, "msisdn_debit": msisdn_debit, "amount": amount, "transid": transid, "date": date, "direction": direction, "num_document": num_document, "nom_document": nom_document, "date_edition": date_edition, "ann_validite": ann_validite, "date_renouvelement": date_renouvelement, "date_expiration": date_expiration, "nom": nom, "prenom": prenom, "seller": seller, "buyer": buyer, "tel_1": tel_1, "tel_2": tel_2, "mail": mail, "seller_tel": seller_tel, "buyer_tel": buyer_tel, "address": address, "seller_address": seller_address, "buyer_address": buyer_address, "child": child, "parental_authority": parental_authority, "nationality": nationality, "date_of_birth": date_of_birth,"place_of_birth": place_of_birth, "sexe": sexe, "company": company, "niu": niu, "rccm": rccm, "type_company": type_company, "type_activity": type_activity, "licence_number": licence_number, "driving_licence_category": driving_licence_category, "num_chassis": num_chassis, "registration": registration, "carte_grise": carte_grise, "old_carte_grise": old_carte_grise, "brand": brand, "model": model, "genre": genre, "type": Type, "engine": engine, "transmission": transmission, "fuel_type": fuel_type, "color": color, "old_color": old_color, "curb_weight": curb_weight, "gross_weight": gross_weight, "power": power, "drivetrain": drivetrain, "taxe_name": taxe_name, "model_year": model_year}

    # Convertir en chaîne JSON
    json_string = json.dumps(json_data, ensure_ascii=False)

    print(json_string)

    curl_command = [
        "curl",
        "-s",
        "-X", "POST",
        "http://10.20.1.4/api/insert_dataset.php",
        "-H", "Content-Type: application/json",
        "-H", "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjExMjUifQ.tsM84PLvbXsvSoNJDTRrSWrfsUKusdRw1jah72v9H08",
        "-d", f"{json_string}"
    ]

    process_curl_command(curl_command)

    # Temps d'attente de 5 secondes
    time.sleep(3)

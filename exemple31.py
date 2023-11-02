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

    json_data = {"msisdn_credit": "", "msisdn_debit": "", "amount": amount, "transid": "", "date": date, "direction": direction, "num_document": num_document, "nom_document": nom_document, "date_edition": date_edition, "ann_validite": ann_validite, "date_renouvelement": "2024-08-30", "date_expiration": "2026-01-01", "nom": "MOTOKOUA", "prenom": "Hegel", "seller": "", "buyer": "", "tel_1": tel_1, "tel_2": "065444242", "mail": "support@besnode.com", "seller_tel": "057360001", "buyer_tel": "065444242", "address": address, "seller_address": "", "buyer_address": "MOUNKONDO MAZALA", "child": child, "parental_authority": "", "nationality": nationality,
                 "date_of_birth": date_of_birth, "place_of_birth": place_of_birth, "sexe": "", "company": company, "niu": niu, "rccm": rccm, "type_company": type_company, "type_activity": type_activity, "licence_number": "AB1234567", "driving_licence_category": driving_licence_category, "num_chassis": num_chassis, "registration": registration, "carte_grise": "", "old_carte_grise": "", "brand": brand, "model": model, "genre": "", "type": "", "engine": "", "transmission": "", "fuel_type": fuel_type, "color": color, "old_color": "NOIR", "curb_weight": "", "gross_weight": "", "power": "", "drivetrain": "", "taxe_name": taxe_name, "model_year": model_year}

    # json_data = {'msisdn_credit': '', 'msisdn_debit': '', 'amount': '50', 'transid': '', 'date': '2023-08-09', 'direction': 'DGTT', 'num_document': 'RV001-0000000012', 'nom_document': 'Redevance pour les véhicules', 'date_edition': '2023-08-09', 'ann_validite': '2023', 'date_renouvelement': '0000-00-00', 'date_expiration': '2023-12-31', 'nom': '', 'prenom': '', 'seller': '', 'buyer': '', 'tel_1': '', 'tel_2': '', 'mail': '', 'seller_tel': '', 'buyer_tel': '', 'address': '', 'seller_address': '', 'buyer_address': '', 'child_age': '', 'parental_authority': '', 'nationality': '', 'date_of_birth': '0000-00-00','place_of_birth': '', 'sexe': '', 'company': 'TEST REDEVANCE 30', 'niu': 'M20191000322031', 'rccm': '', 'type_company': '', 'type_activity': '', 'licence_number': '', 'driving_licence_category': '', 'num_chassis': 'TESLA9000MDY29299', 'registration': '700XS5', 'carte_grise': '', 'old_carte_grise': '', 'brand': 'Tesla', 'model': 'Model Y', 'genre': '', 'type': '', 'engine': '', 'transmission': '', 'fuel_type': '', 'color': 'ROUGE', 'old_color': '', 'curb_weight': '', 'gross_weight': '', 'power': '', 'drivetrain': '', 'model_year': '', 'taxe_name': 'Redevance annuelle Auto-École/Moyenne entreprise'}

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

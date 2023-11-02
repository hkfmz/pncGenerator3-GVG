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

    # json_data = {"msisdn_credit":"","msisdn_debit":"","amount":amount,"transid":"","date":date,"direction":direction,"num_document":num_document,"nom_document":nom_document,"date_edition":date_edition,"ann_validite":ann_validite,"date_renouvelement":"2024-08-30","date_expiration":"2026-01-01","nom":"","prenom":"","seller":"","buyer":"","tel_1":tel_1,"tel_2":"","mail":"","seller_tel":"","buyer_tel":"","address":address,"seller_address":"","buyer_address":"","child":"","parental_authority":"","nationality":"","date_of_birth":"0000-00-00","place_of_birth":"","sexe":"","company":company,"niu":niu,"rccm":rccm,"type_company":type_company,"type_activity":type_activity,"licence_number":"","driving_licence_category":"","num_chassis":num_chassis,"registration":registration,"carte_grise":"","old_carte_grise":"","brand":brand,"model":model,"genre":"","type":"","engine":"","transmission":"","fuel_type":"","color":color,"old_color":"","curb_weight":"","gross_weight":"","power":"","drivetrain":"","taxe_name":taxe_name,"model_year":""}

    # json_data = {'msisdn_credit': '', 'msisdn_debit': '', 'amount': '50', 'transid': '', 'date': '2023-08-09', 'direction': 'DGTT', 'num_document': 'RV001-0000000012', 'nom_document': 'Redevance pour les véhicules', 'date_edition': '2023-08-09', 'ann_validite': '2023', 'date_renouvelement': '0000-00-00', 'date_expiration': '2023-12-31', 'nom': '', 'prenom': '', 'seller': '', 'buyer': '', 'tel_1': '', 'tel_2': '', 'mail': '', 'seller_tel': '', 'buyer_tel': '', 'address': '', 'seller_address': '', 'buyer_address': '', 'child_age': '', 'parental_authority': '', 'nationality': '', 'date_of_birth': '0000-00-00','place_of_birth': '', 'sexe': '', 'company': 'TEST REDEVANCE 30', 'niu': 'M20191000322031', 'rccm': '', 'type_company': '', 'type_activity': '', 'licence_number': '', 'driving_licence_category': '', 'num_chassis': 'TESLA9000MDY29299', 'registration': '700XS5', 'carte_grise': '', 'old_carte_grise': '', 'brand': 'Tesla', 'model': 'Model Y', 'genre': '', 'type': '', 'engine': '', 'transmission': '', 'fuel_type': '', 'color': 'ROUGE', 'old_color': '', 'curb_weight': '', 'gross_weight': '', 'power': '', 'drivetrain': '', 'model_year': '', 'taxe_name': 'Redevance annuelle Auto-École/Moyenne entreprise'}

    # json_data = {'msisdn_credit': '', 'msisdn_debit': '', 'amount': '50', 'transid': '', 'date': '2023-08-15', 'direction': 'DGTT', 'num_document': 'RE001-0000000024', 'nom_document': 'Redevance pour les sociétés', 'date_edition': '2023-08-15', 'ann_validite': '2023', 'date_renouvelement': '2024-08-30', 'date_expiration': '2023-12-31', 'nom': 'Delmas', 'prenom': 'Herve', 'seller': '', 'buyer': '', 'tel_1': '242065444249', 'tel_2': '', 'mail': '', 'seller_tel': '', 'buyer_tel': '', 'address': 'Rue de la joie de vivre', 'seller_address': '', 'buyer_address': '', 'child_age': '', 'parental_authority': '', 'nationality': 'CONGOLAISE','date_of_birth': '1989-06-02', 'place_of_birth': 'Kinshasa', 'sexe': '', 'company': 'CHEZDAMS', 'niu': 'M141460603232888', 'rccm': 'CG-BZV-01-3456789987-6545', 'type_company': 'Petite', 'type_activity': 'Vente de Véhicule', 'licence_number': '', 'driving_licence_category': '', 'num_chassis': '', 'registration': '', 'carte_grise': '', 'old_carte_grise': '', 'brand': '', 'model': '', 'genre': '', 'type': '', 'engine': '', 'transmission': '', 'fuel_type': '', 'color': '', 'old_color': '', 'curb_weight': '', 'gross_weight': '', 'power': '', 'drivetrain': '', 'model_year': '', 'taxe_name': 'Redevance annuelle vente de véhicule/Moyenne entreprise'}

    json_data = {"msisdn_credit": "242044502001", "msisdn_debit": "242046802001", "amount": 5227, "transid": " ", "date": "2023-09-02", "direction": "DGTT", "num_document": "TEST-0002", "nom_document": "Certificat dauthenticité du permis de conduire", "date_edition": "2023-09-02", "ann_validite": "2024-12-31", "date_renouvelement": "2024-05-09", "date_expiration": "2024-12-31", "nom": "Nom 2", "prenom": "Prenom 2", "seller": "Vendeur 2", "buyer": "Acheteur 2", "tel_1": "057360001", "tel_2": "067360001", "mail": "support@besnode.com", "seller_tel": "065444243", "buyer_tel": "057360001", "address": "46, Rue Vinza Tie-Tie Pointe-Noire", "seller_address": "45, Rue Mvoumvou Pointe-Noire", "buyer_address": "15, Rue Nazareth Nkombo BZ", "child": "Steven MOKOKO", "parental_authority": "Stéphane MOKOKO","nationality": "Congolaise", "date_of_birth": "1991-08-15", "place_of_birth": "Ouesso", "sexe": "Mr", "company": "BES-SARL", "niu": "20182002322002", "rccm": "CG-BZV2002 - B35002", "type_company": "Petite", "type_activity": "Garage", "licence_number": "PC123456790", "driving_licence_category": "Catégorie A2", "num_chassis": "PK04939KLZ0Z00260", "registration": "405EG4", "carte_grise": "2017TL15887", "old_carte_grise": "2017MV15989", "brand": "Alfa Romeo", "model": "Spider", "genre": "Berline", "type": "Bus", "engine": "Moteur V9", "transmission": "Mannuelle", "fuel_type": "Essence", "color": "BLANC", "old_color": "NOIR", "curb_weight": 1899, "gross_weight": 2891, "power": 204, "drivetrain": "AWD", "taxe_name": "Certificat d'authenticité du permis de conduire", "model_year": "1989-06-03"}

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

# Скрипт для создания изменения пользователей в Яндекс
# CSV выгружается powershall скриптом AD_users.ps1
# Инфа по сотруднику: externalId - табельный номер, nickname - логин, name - ФИО, departmentId - подразделение, position - Должность, contacts - Контакты, password - Временный пароль]
#

import os
import csv

from dotenv import load_dotenv

from python_script_example.lib.y360_api.api_script import API360

csv_file = 'c:\\temp\\AD_users.csv'
password = ''
#users_add = []
company_departments_id = {}
users_id_yandex = {}

if __name__ == "__main__":
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    organization = API360(os.environ.get('orgId'), os.environ.get('access_token'))


    #Загруаем структуру компании из облака в справочник
    departaments = organization.get_departments_list()
    for i in departaments:
        company_departments_id[i['name']] = i['id']
    
    # Загружаем пользователей из облака
    users_yandex = organization.get_all_users()
    for i in users_yandex:
        users_id_yandex[i['nickname']] = i['id']

    with open(csv_file, newline='', encoding="utf-8") as csvfile:   # Формируем список пользователей для загрузки в Яндекс
        reader = csv.DictReader(csvfile)
        for i in reader:
            contacts = []
            name = {}
            nickname = i['SamAccountName']
            nickname = nickname.lower()
            name_full = nickname.split(".")
            name['first'] = name_full[0]
            name['last'] = name_full[1]
            departmentName_list = i['DistinguishedName'].split(",")
            departmentName = departmentName_list[2][3:]
            departmentId = company_departments_id[departmentName]
            externalId = i['Description']
            position = i['Title']
            MobilePhone = i['MobilePhone']
            Phone =  i['telephoneNumber']
            contacts_phone = {'type': 'phone', 'value': MobilePhone}
            contacts_mail = {'type': 'phone_extension', 'value': Phone}
            contacts.append(contacts_phone)
            contacts.append(contacts_mail)
            user_ad = {
                "contacts": contacts,
                "departmentId": departmentId,
                "externalId": externalId,
                "position": position
            }
            if nickname in users_id_yandex.keys():
                user_id = users_id_yandex[nickname]
                create_user_yandex = organization.patch_user_info(user_id, user_ad)
                print(f"Данные пользователя {nickname} {user_id} обновлены")                
            else:
                print(f"Пользователя {nickname} нет")

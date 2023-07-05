import requests


async def get_data_entity(guid, who):
    headers_guid = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Referer": "https://fedresurs.ru/person/"+guid,
    }

    if who == "ur":
        response_json_entity_ur = {}
        url_guid_ur = "https://fedresurs.ru/backend/companies/"+guid
        response_entity_ur = requests.get(url_guid_ur, headers=headers_guid)
        data = response_entity_ur.json()

        if "fullName" in data["companyInfo"]:
            response_json_entity_ur['fullName'] = data["companyInfo"]["fullName"]
        
        if "egrulAddress" in data["companyInfo"]:
            response_json_entity_ur['egrulAddress'] = data["companyInfo"]["egrulAddress"]

        if "ogrn" in data["companyInfo"]:
            response_json_entity_ur['ogrn'] = data["companyInfo"]["ogrn"]

        if "inn" in data["companyInfo"]:
            response_json_entity_ur['inn'] = data["companyInfo"]["inn"]
        
        for item in data["legalCases"]:
            response_json_entity_ur['legalCases'] = data["legalCases"]

        return(response_json_entity_ur)   
            
    if who == "fiz": 
        response_json_entity_fiz = {}
        url_guid_fiz = "https://fedresurs.ru/backend/persons/"+guid
        response_entity_fiz = requests.get(url_guid_fiz, headers=headers_guid)
        data = response_entity_fiz.json()
    
        if "fullName" in data["info"]:
            response_json_entity_fiz['fullName'] = data["info"]["fullName"]

        if "address" in data["info"]:
            response_json_entity_fiz['address'] = data["info"]["address"]

        if "inn" in data["info"]:
            response_json_entity_fiz['inn'] = data["info"]["inn"]

        if "snils" in data["info"]:
            response_json_entity_fiz['snils'] = data["info"]["snils"]

        if "birthdateBankruptcy" in data["info"]:
            response_json_entity_fiz['birthdateBankruptcy'] = data["info"]["birthdateBankruptcy"]


        if "birthplaceBankruptcy" in data["info"]:
            response_json_entity_fiz['birthplaceBankruptcy'] = data["info"]["birthplaceBankruptcy"]

        if "ogrnipHistories" in data["info"]:
            if len(data["info"]["ogrnipHistories"])!= 0:
                response_json_entity_fiz['ogrnipHistories'] = data["info"]["ogrnipHistories"]

        if "nameHistories" in data["info"]:
            if len(data["info"]["nameHistories"])!= 0:
                response_json_entity_fiz['nameHistories'] = data["info"]["nameHistories"]

        return(response_json_entity_fiz)
import requests
from services.data_entity import get_data_entity


async def get_data_search(type, search, status, region):
    headers_search = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Referer": "https://bankrot.fedresurs.ru",
    "Host": "bankrot.fedresurs.ru"
    }

    response_json = []

    if type == 1:
        
        url_ur  = "https://bankrot.fedresurs.ru/backend/cmpbankrupts?searchString="+search+"&isActiveLegalCase="+status+"&regionId="+region+"&limit=15&offset=0"
        response_ur = requests.get(url_ur, headers=headers_search)
        guids_ur = response_ur.json()

        if len(guids_ur["pageData"])!= 0:
            for item in guids_ur["pageData"]:
                response_json_entity_ur = await get_data_entity(item["guid"], "ur")
                response_json.append(response_json_entity_ur)

        else:
            response_json.append("По вашему запросу не найдено ни одного совпадения, попробуйте изменить поисковую фразу")

    if type == 2:
        url_fiz = "https://bankrot.fedresurs.ru/backend/prsnbankrupts?searchString="+search+"&isActiveLegalCase="+status+"&regionId="+region+"&limit=15&offset=0"
        response_fiz = requests.get(url_fiz, headers=headers_search)
        guids_fiz = response_fiz.json()

        if len(guids_fiz["pageData"])!= 0:
            for item in guids_fiz["pageData"]:
                response_json_entity_fiz = await get_data_entity(item["guid"], "fiz")
                response_json.append(response_json_entity_fiz)

        else:
            response_json.append("По вашему запросу не найдено ни одного совпадения, попробуйте изменить поисковую фразу")

    return(response_json)

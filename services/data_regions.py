from requests import get


async def get_region_all():
    headers_search = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Referer": "https://bankrot.fedresurs.ru",
    "Host": "bankrot.fedresurs.ru"
    }

    url_regions = "https://bankrot.fedresurs.ru/backend/referencebook/regions"
    response_regions = get(url_regions, headers=headers_search)

    return(response_regions.json())

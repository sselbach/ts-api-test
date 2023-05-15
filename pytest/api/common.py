import os

import requests

from typing import Optional

def api_request(endpoint: str, headers: dict = None) -> requests.Response:
    api_base_url = os.environ.get("API_BASE_URL")
    api_key = os.environ.get("API_KEY")


    res = requests.get(api_base_url + endpoint, headers={
        "X-APIKEY": api_key
    })

    return res


def response_json(res: requests.Response) -> Optional[dict]:
    try:
        content = res.json()
    
    except requests.exceptions.JSONDecodeError:
        content = None

    return content
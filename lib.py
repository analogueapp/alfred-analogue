import sys
import json
from workflow import Workflow, ICON_WEB, web


def search_user_logs():
    """
    search current user logs/content
    """
    url = "https://www.analogue.app/api/logs"
    # Todo: Get username via the env config or using auth
    params = dict(username="hugh", tag="", limit=10, offset=0, collection=True)
    r = web.get(url, params)

    # throw an error if request failed
    # Workflow will catch this and show it to the user
    r.raise_for_status()

    # Parse the JSON returned by pinboard and extract the posts
    result = r.json()["data"]

    return result


def search_analogue(query):
    """
    Search all of analogue for a specific piece of content
    """
    # TODO: host this under a proper microservice
    url = "https://pysrv.now.sh/analogue/search"

    # TODO: Get username via the env config or using auth
    params = dict(q=query)

    r = web.get(url, params)

    # throw an error if request failed
    # Workflow will catch this and show it to the user
    r.raise_for_status()

    # Parse the JSON returned by pinboard and extract the posts
    result = r.json()["hits"]

    return result

def get_token(email, password):
    """
    Get user token for API calls
    """
    r = web.post(
        url="https://www.analogue.app/api/users/login",
        params=None,
        headers={
                "Connection": "keep-alive",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
                "Content-Type": "application/json",
                "Accept": "*/*",
                "Origin": "https://www.analogue.app",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://www.analogue.app/login",
                "Accept-Language": "en-US,en;q=0.9",
                "Cookie": "ajs_group_id=null; ajs_anonymous_id=%22453c9e9b-20d9-464b-9b2f-544d08c4517c%22; ajs_user_id=%228503%22; _lr_uf_-9zropr=1f5d3d9a-7af1-478a-af9a-9bdd499187e6; amplitude_idundefinedanalogue.app=eyJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOm51bGwsImxhc3RFdmVudFRpbWUiOm51bGwsImV2ZW50SWQiOjAsImlkZW50aWZ5SWQiOjAsInNlcXVlbmNlTnVtYmVyIjowfQ==; _lr_tabs_-9zropr%2Fanalogue={%22sessionID%22:0%2C%22recordingID%22:%224-6ccf0dab-5235-4d33-a78a-0693d0268674%22%2C%22lastActivity%22:1588357409717}; _lr_hb_-9zropr%2Fanalogue={%22heartbeat%22:1588357409717}; mp_42c2d87f255cdb53a9581d2596fe60d6_mixpanel=%7B%22distinct_id%22%3A%20%228503%22%2C%22%24device_id%22%3A%20%22171a213b18430e-0029530280115b-39687506-13c680-171a213b185a21%22%2C%22mp_lib%22%3A%20%22Segment%3A%20web%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22%24user_id%22%3A%20%228503%22%2C%22mp_name_tag%22%3A%20%22hughmil3s%40gmail.com%22%2C%22type%22%3A%20%22consumer%22%2C%22id%22%3A%20%228503%22%2C%22%24email%22%3A%20%22hughmil3s%40gmail.com%22%2C%22%24first_name%22%3A%20%22Hugh%22%2C%22%24last_name%22%3A%20%22A.%20Miles%20II%22%2C%22%24name%22%3A%20%22Hugh%20A.%20Miles%20II%22%2C%22%24username%22%3A%20%22hugh%22%7D; amplitude_id_4bf7a5f993ab7a9311ed9393614f20c5analogue.app=eyJkZXZpY2VJZCI6IjAwNDJmZGM2LTY0OTktNDY4Yi1hZjFhLTEzOTFjOTI5MGFiYVIiLCJ1c2VySWQiOiI4NTAzIiwib3B0T3V0IjpmYWxzZSwic2Vzc2lvbklkIjoxNTg4MzU2NTY1NzE2LCJsYXN0RXZlbnRUaW1lIjoxNTg4MzU3NDE5MTA2LCJldmVudElkIjoxNTAsImlkZW50aWZ5SWQiOjQ3LCJzZXF1ZW5jZU51bWJlciI6MTk3fQ==",
                "Accept-Encoding": "gzip",
            },
        cookies=None,
        files=None,
        auth=None,
        timeout=60,
        allow_redirects=False,
        stream=False,
        data=json.dumps({
                "user": {
                    "email": email,
                    "password": password
                }
        }))   
    
    return r.json()['user']['token']
import sys
from workflow import Workflow, ICON_WEB, web

class Analogue:
    def __init__(self):
        pass

    def search_user_logs(self):
        """
        search current user logs/content
        """
        url = 'https://www.analogue.app/api/logs'
        # Todo: Get username via the env config or using auth
        params = dict(
            username='hugh', 
            tag='',
            limit=10,
            offset=0,
            collection=True
        )
        r = web.get(url, params)

        # throw an error if request failed
        # Workflow will catch this and show it to the user
        r.raise_for_status()

        # Parse the JSON returned by pinboard and extract the posts
        result = r.json()['data']

        return result

    def search_analogue(self):
        """
	    Search all of analogue for a specific piece of content
        """
        pass
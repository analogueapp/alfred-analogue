import sys
from workflow import Workflow, ICON_WEB, web

class Analogue:
    def search_user_logs(wf):
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

        # Loop through the returned posts and add an item for each to
        # the list of results for Alfred
        for log in result:
        
        # The user is tagged in the url query action
        wf.add_item(title=log['content']['title'],
                    subtitle=log['content']['excerpt'],
		    valid=True,
                    arg="https://analogue.app/link/{}/".format(log['content']['slug']),
                    icon=log['content']['imageUrl'])

        # Send the results to Alfred as XML
        wf.send_feedback()

	
    def search_analogue():
	"""
	Search all of analogue for a specific piece of content
    """
		pass


    

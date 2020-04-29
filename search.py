import sys
from workflow import Workflow, ICON_WEB, web
from lib import Analogue

def main(wf):
	     # Get query from Alfred
	if len(wf.args):
		query = wf.args[0]
	else:
		query = None
	url = 'https://pysrv.now.sh/analogue/search'
    	# Todo: Get username via the env config or using auth
    	params = dict(
		q=query
    	)
    	r = web.get(url, params)

    	# throw an error if request failed
    	# Workflow will catch this and show it to the user
    	r.raise_for_status()

    	# Parse the JSON returned by pinboard and extract the posts
    	result = r.json()['hits']

    	# Loop through the returned posts and add an item for each to
    	# the list of results for Alfred
    	for hit in result:
       		# The user is tagged in the url query action
        	wf.add_item(title=hit['title'],
			subtitle=hit['excerpt'],
			valid=True,
			arg="https://analogue.app/link/{}/".format(hit['slug']),
			icon=hit['image_url'])
	
	# Send the results to Alfred as XML
	wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))

import sys
from workflow import Workflow, ICON_WEB, web

API_KEY = 'your-pinboard-api-key'


def main(wf):
    url = 'https://pysrv.now.sh/'
    # params = dict(auth_token=API_KEY, count=20, format='json')
    r = web.get(url)

    # throw an error if request failed
    # Workflow will catch this and show it to the user
    r.raise_for_status()

    # Parse the JSON returned by pinboard and extract the posts
    result = r.json()

    # Loop through the returned posts and add an item for each to
    # the list of results for Alfred
    for planet in result['hello']:
        wf.add_item(title=planet,
                    subtitle=planet,
                    icon=ICON_WEB)

    # Send the results to Alfred as XML
    wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
